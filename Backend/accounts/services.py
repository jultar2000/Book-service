import logging
from smtplib import SMTPException

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from accounts.models import account_activation_token
from utils.exceptionhandler import CustomApiException
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken

custom_user = get_user_model()


def create_user(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if password1 and password2:
        if password1 != password2:
            raise CustomApiException('Passwords must match', 400)
        try:
            validate_password(password1)
        except ValidationError as ex:
            raise CustomApiException(ex, 400)

    try:
        user = custom_user.objects.create_user(
            username=username,
            email=email,
            password=password1,
            is_active=True)
    except IntegrityError as ex:
        raise CustomApiException(ex.__cause__.__str__(), 400)

    email_template = render_to_string('email.html', {
        'user': username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })

    send_email('BookService account activation', '',
               'BookService@gmail.com', [email],
               email_template)

    return user


def activate_accounts(uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = custom_user.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, custom_user.DoesNotExist) as ex:
        return CustomApiException(ex, 400)

    if account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return

    return CustomApiException('Invalid token, token may been already used.', 400)


def send_email(subject, message, from_email, recipient, html_message):
    try:
        send_mail(subject=subject,
                  message=message,
                  recipient_list=recipient,
                  from_email=from_email,
                  html_message=html_message)

    except SMTPException as ex:
        raise CustomApiException(ex, 400)


def blacklist_token(data):
    try:
        refresh_token = data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
    except Exception as ex:
        raise CustomApiException(ex, 400)
