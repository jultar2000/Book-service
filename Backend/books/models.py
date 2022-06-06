from versatileimagefield.fields import VersatileImageField, PPOIField
from django.db import models

GENRE_CHOICES = {
    ('SCF', 'Science-fiction'),
    ('HOR', 'Horror'),
    ('THR', 'Thriller'),
    ('HIS', 'Historical'),
    ('FAN', 'Fantasy')
}

class Book(models.Model):
    title = models.CharField(max_length=70, default=None, null=False, blank=False)
    pages_number = models.IntegerField(default=None, null=False, blank=False)
    publishment_year = models.IntegerField(default=None, null=False, blank=False)
    description = models.CharField(max_length=600, default=None, null=False, blank=False)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=3, default=None, null=False, blank=False)
    image = VersatileImageField(ppoi_field='image_ppoi', default=None, null=False, blank=False)
    image_ppoi = PPOIField()


