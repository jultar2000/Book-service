from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderSerializer
from .services import add_order_item_to_cart
from rest_framework.response import Response
from rest_framework import status


class OrderItemViewSet(ListModelMixin,
                       CreateModelMixin,
                       UpdateModelMixin,
                       RetrieveModelMixin,
                       GenericViewSet):

    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()

    def create(self, request, *args, **kwargs):
        add_order_item_to_cart(request)
        return Response('Item added to cart', status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = OrderItem.objects.filter(custom_user=request.user)
        serializer = OrderItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderViewSet(RetrieveModelMixin,
                   UpdateModelMixin,
                   ListModelMixin,
                   GenericViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
