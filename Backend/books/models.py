from versatileimagefield.fields import VersatileImageField, PPOIField
from django.db import models
from authors.models import Author

GENRE_CHOICES = {
    ('SCF', 'Science-fiction'),
    ('HOR', 'Horror'),
    ('THR', 'Thriller'),
    ('HIS', 'Historical'),
    ('FAN', 'Fantasy')
}


class Book(models.Model):
    title = models.CharField(max_length=70, default=None, null=True, blank=False)
    pages_number = models.IntegerField(default=None, null=True, blank=False)
    publishment_year = models.IntegerField(default=None, null=True, blank=False)
    description = models.CharField(max_length=600, default=None, null=True, blank=False)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=3, default=None, null=True, blank=False)
    price = models.FloatField(default=None, null=True, blank=False)
    discount_percentage = models.FloatField(default=None, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    image = VersatileImageField(ppoi_field='image_ppoi', default=None, null=False, blank=False)
    image_ppoi = PPOIField()
