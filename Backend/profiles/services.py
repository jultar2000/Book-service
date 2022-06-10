from django.contrib.auth import get_user_model
from .models import CustomProfile
from django.core.exceptions import ValidationError
from utils.exceptionhandler import CustomApiException


def update_profile(request):
    data = request.data
    custom_profile = CustomProfile.objects.get(custom_user=request.user.id)
    for key, value in data:
        custom_profile.key = value
    custom_profile.save()
