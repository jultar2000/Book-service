from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import CustomProfile

custom_user = get_user_model()


@receiver(post_save, sender=custom_user)
def create_custom_profile(sender, instance, created, **kwargs):
    if created:
        CustomProfile.objects.create(custom_user=instance)
