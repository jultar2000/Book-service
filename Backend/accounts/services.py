from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from utils.exceptionhandler import CustomApiException

custom_user = get_user_model()


def create_user(data):
    password1 = data.get('password1')
    password2 = data.get('password2')

    if password1 and password2:
        if password1 != password2:
            raise CustomApiException(400, 'Passwords must match')
        try:
            validate_password(password1)
        except ValidationError as ex:
            raise CustomApiException(400, ex)

    user = custom_user.objects.create_user(
        username=data.get('username'),
        email=data.get('email'),
        password=password1,
        is_active=False)
    return user
