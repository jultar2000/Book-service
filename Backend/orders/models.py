from django.db import models
from accounts.models import CustomProfile, Address


class Order(models.Model):
    custom_profile = models.ForeignKey(CustomProfile, on_delete=models.CASCADE)
    order_date = models.DateField()
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_adress', on_delete=models.CASCADE)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', on_delete=models.CASCADE)

