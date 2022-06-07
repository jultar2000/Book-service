from versatileimagefield.fields import VersatileImageField, PPOIField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django_countries.fields import CountryField
from django.utils import six
from django.db import models

GENDER_CHOICES = {
    ('M', 'Male'),
    ('F', 'Female')
}

ADDRESS_CHOICES = {
    ('B', 'Billing'),
    ('S', 'Shipping')
}


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, blank=False,
                                help_text="Username is needed, 40 characters or fewer.")
    password = models.CharField(max_length=128, blank=False)
    email = models.EmailField(unique=True, blank=False)
    is_active = models.BooleanField(default=False, blank=False)
    first_name = models.CharField(max_length=40, default=None, null=True, blank=True)
    last_name = models.CharField(max_length=40, default=None, null=True, blank=True)


class CustomProfile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    birth_date = models.DateField(default=None, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None, null=True, blank=True)
    image = VersatileImageField(ppoi_field="image_ppoi", default=None, null=True, blank=True)
    image_ppoi = PPOIField()


class Address(models.Model):
    custom_profile = models.ForeignKey(CustomProfile, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    apartment_num = models.IntegerField(default=None, null=True, blank=True)
    house_num = models.IntegerField(default=None, null=True, blank=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active))


account_activation_token = TokenGenerator()
