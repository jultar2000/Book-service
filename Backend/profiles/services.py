from .models import CustomProfile


def update_profile(data, user):
    custom_profile = CustomProfile.objects.get(custom_user=user)
    for key, value in data.items():
        setattr(custom_profile, key, value)
    custom_profile.save()
