from versatileimagefield.fields import VersatileImageField, PPOIField
from django_countries.fields import CountryField
from accounts.models import CustomUser
from django.db import models


GENDER_CHOICES = {
    ('M', 'Male'),
    ('F', 'Female')
}

ADDRESS_CHOICES = {
    ('B', 'Billing'),
    ('S', 'Shipping')
}


class CustomProfile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, default=None, null=True, blank=True)
    last_name = models.CharField(max_length=40, default=None, null=True, blank=True)
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
