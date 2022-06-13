from django.contrib.auth import get_user_model
from .models import CustomProfile
from django.core.exceptions import ValidationError
from utils.exceptionhandler import CustomApiException


def update_profile(data, user):
    custom_profile = CustomProfile.objects.get(custom_user=user)
    for key, value in data.items():
        setattr(custom_profile, key, value)
    custom_profile.save()
