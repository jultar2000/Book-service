from rest_framework.permissions import IsAuthenticated

from .models import OrderItem
from .serializers import OrderItemSerializer
from .services import add_order_item_to_cart
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView


class ListCreateItemView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        add_order_item_to_cart(request)
        return Response('Item added to cart', status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = OrderItem.objects.filter(custom_user=request.user)
        serializer = OrderItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateItemView(UpdateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
