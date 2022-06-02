from versatileimagefield.fields import VersatileImageField, PPOIField
from django.db import models


class Book(models.Model):
    image = VersatileImageField(ppoi_field='image_ppoi', null=True)
    image_ppoi = PPOIField()
    title = models.CharField(max_length=70, default=None)
    pages_number = models.IntegerField(default=None)
    publishment_year = models.IntegerField(default=None)
    description = models.CharField(max_length=600, default=None)

