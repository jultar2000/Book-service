from versatileimagefield.fields import VersatileImageField, PPOIField
from django.db import models
from authors.models import Author
from django.core.validators import MaxValueValidator, MinValueValidator

GENRE_CHOICES = {
    ('SCF', 'Science-fiction'),
    ('HOR', 'Horror'),
    ('THR', 'Thriller'),
    ('HIS', 'Historical'),
    ('FAN', 'Fantasy')
}


class Book(models.Model):
    title = models.CharField(max_length=70)
    pages_number = models.PositiveIntegerField(null=True)
    publishment_year = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=600)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=3)
    price = models.FloatField(null=True, validators=[MinValueValidator(0)])
    discount_percentage = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(100)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    image = VersatileImageField(ppoi_field='image_ppoi', null=False)
    image_ppoi = PPOIField()

    @property
    def current_price(self):
        return self.price * (100 - self.discount_percentage) / 100
