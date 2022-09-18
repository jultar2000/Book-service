from rest_framework import serializers
from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    book_cover = serializers.CharField(allow_blank=False)
    book_language = serializers.CharField(allow_blank=False)

    class Meta:
        model = OrderItem
        fields = ("book",
                  "order",
                  "quantity",
                  "book_cover",
                  "book_language")


class RetrieveOrderItemSerializer(OrderItemSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta(OrderItemSerializer.Meta):
        fields = OrderItemSerializer.Meta.fields + ("id", "total_price",)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("order_date",
                  "ordered",
                  "status",
                  "shipping_address",
                  "billing_address")


class RetrieveOrderSerializer(OrderSerializer):
    total_order_price = serializers.ReadOnlyField()

    class Meta(OrderSerializer.Meta):
        fields = OrderSerializer.Meta.fields + ("id", "total_order_price",)
