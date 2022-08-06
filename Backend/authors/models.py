from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

from profiles.models import GENDER_CHOICES
from django_countries.fields import CountryField


class Author(models.Model):
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    country = CountryField(multiple=False, null=True)
    image = VersatileImageField(ppoi_field="image_ppoi", null=True)
    image_ppoi = PPOIField()
