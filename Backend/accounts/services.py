from smtplib import SMTPException

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from accounts.models import account_activation_token
from utils.exceptionhandler import CustomApiException
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

custom_user = get_user_model()


def create_user(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if password1 and password2:
        if password1 != password2:
            raise CustomApiException(400, 'Passwords must match')
        try:
            validate_password(password1)
        except ValidationError as ex:
            raise CustomApiException(400, ex)

    try:
        user = custom_user.objects.create_user(
            username=username,
            email=email,
            password=password1,
            is_active=False)
    except IntegrityError as ex:
        raise CustomApiException(400, ex.__cause__.__str__())

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


def send_email(subject, message, from_email, recipient, html_message):
    try:
        send_mail(subject=subject,
                  message=message,
                  recipient_list=recipient,
                  from_email=from_email,
                  html_message=html_message)

    except SMTPException as ex:
        raise CustomApiException(400, ex)
