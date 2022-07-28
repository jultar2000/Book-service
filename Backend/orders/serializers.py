from rest_framework import serializers
from django.db import models
from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    book_id = models.PositiveIntegerField()

    class Meta:
        model = OrderItem
        fields = ("id",
                  "book_id",
                  "quantity",
                  "book_cover",
                  "book_language")
