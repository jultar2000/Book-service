from django.db import models
from profiles.models import CustomProfile, Address
from books.models import Book

STATUS_CHOICES = {
    ('P', 'BEING PREPARED'),
    ('S', 'BEING DELIVERED'),
    ('R', 'RECEIVED')
}


class Order(models.Model):
    custom_profile = models.ForeignKey(CustomProfile, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    order_date = models.DateField(default=None, null=True)
    ordered = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=None)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_adress', on_delete=models.CASCADE, null=True)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', on_delete=models.CASCADE, null=True)
