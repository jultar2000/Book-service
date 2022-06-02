from versatileimagefield.fields import VersatileImageField, PPOIField
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, blank=False,
                                help_text="Username is needed, 40 characters or fewer.")
    password = models.CharField(max_length=128, blank=False)
    email = models.EmailField(blank=False)
    is_active = models.BooleanField(default=False, blank=False)
    first_name = models.CharField(max_length=40, default=None, blank=True)
    last_name = models.CharField(max_length=40, default=None, blank=True)


class CustomProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE'
        FEMALE = 'FEMALE'

    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    birth_date = models.DateField(default=None, blank=True)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=None)
    image = VersatileImageField(ppoi_field="image_ppoi")
    image_ppoi = PPOIField()


