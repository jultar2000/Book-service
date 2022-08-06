from rest_framework import serializers
from django.db import models
from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    total_order_price = serializers.Field(required=False)

    class Meta:
        model = OrderItem
        fields = ("id",
                  "book",
                  "quantity",
                  "book_cover",
                  "book_language",
                  "total_order_price")


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.Field(required=False)

    class Meta:
        model = OrderItem
        fields = ("id",
                  "order_date",
                  "ordered",
                  "status",
                  "shipping_address",
                  "billing_address",
                  "total_price")
