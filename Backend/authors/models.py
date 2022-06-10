from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

from profiles.models import GENDER_CHOICES
from django_countries.fields import CountryField


class Author(models.Model):
    first_name = models.CharField(max_length=40, default=None, null=True, blank=True)
    last_name = models.CharField(max_length=40, default=None, null=True, blank=True)
    birth_date = models.DateField(default=None, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=None, null=True, blank=True)
    country = CountryField(multiple=False)
    image = VersatileImageField(ppoi_field="image_ppoi", default=None, null=True, blank=True)
    image_ppoi = PPOIField()
