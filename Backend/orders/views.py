from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView

from .models import OrderItem
from .serializers import OrderItemSerializer
from .services import add_order_item_to_cart
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers


class OrderItemView(APIView):
    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            add_order_item_to_cart(request)
            return Response('Item added to cart', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(serializers.serialize('python', OrderItem.objects.all()),
                        status=status.HTTP_200_OK)
