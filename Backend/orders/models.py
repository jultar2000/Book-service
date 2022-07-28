from django.db import models
from profiles.models import Address, CustomProfile
from books.models import Book

STATUS_CHOICES = {
    ('P', 'BEING PREPARED'),
    ('S', 'BEING DELIVERED'),
    ('R', 'RECEIVED')
}

COVER_CHOICES = {
    ('H', 'HARD'),
    ('S', 'SOFT')
}

BOOK_LANGUAGE = {
    ('E', 'ENGLISH'),
    ('P', 'POLISH')
}


class Order(models.Model):
    custom_profile = models.ForeignKey(CustomProfile, related_name='custom_profile',
                                       on_delete=models.CASCADE, null=True)
    order_date = models.DateField(default=None, null=True)
    active = models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=None)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', on_delete=models.CASCADE, null=True)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', on_delete=models.CASCADE, null=True)

    def get_total_order_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += item.get_total_price()
        return total_price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True)
    book = models.OneToOneField(Book, related_name='book', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    book_cover = models.CharField(choices=COVER_CHOICES, max_length=1, default=None)
    book_language = models.CharField(choices=BOOK_LANGUAGE, max_length=1, default=None)

    def get_total_price(self):
        return self.quantity * self.book.current_price
