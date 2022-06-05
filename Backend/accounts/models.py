from versatileimagefield.fields import VersatileImageField, PPOIField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, blank=False,
                                help_text="Username is needed, 40 characters or fewer.")
    password = models.CharField(max_length=128, blank=False)
    email = models.EmailField(unique=True, blank=False)
    is_active = models.BooleanField(default=False, blank=False)
    first_name = models.CharField(max_length=40, default=None, null=True, blank=True)
    last_name = models.CharField(max_length=40, default=None, null=True, blank=True)


class CustomProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE'
        FEMALE = 'FEMALE'

    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    birth_date = models.DateField(default=None, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=Gender.choices, default=None, null=True, blank=True)
    image = VersatileImageField(ppoi_field="image_ppoi", default=None, null=True, blank=True)
    image_ppoi = PPOIField()


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active))


account_activation_token = TokenGenerator()
