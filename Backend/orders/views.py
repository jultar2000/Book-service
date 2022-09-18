from rest_framework.generics import DestroyAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ViewSet

from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderSerializer, RetrieveOrderItemSerializer, RetrieveOrderSerializer
from .services import add_order_item_to_cart, \
    retrieve_order_item, retrieve_order, update_order_item, update_order
from rest_framework.response import Response
from rest_framework import status


class OrderItemViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            add_order_item_to_cart(serializer.validated_data, request.user)
            return Response('Item added to cart', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            update_order_item(serializer, request.user, pk)
            return Response({'Account successfully updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        order_item = retrieve_order_item(request.user, pk=pk)
        serializer = RetrieveOrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # why when pk not specified all objects are deleted?
    def destroy(self, request, pk=None):
        retrieve_order_item(request.user, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        queryset = OrderItem.objects.filter(custom_user=request.user)
        serializer = RetrieveOrderItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderViewSet(RetrieveModelMixin,
                   UpdateModelMixin,
                   ListModelMixin,
                   DestroyAPIView,
                   GenericViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()

    def retrieve(self, request, *args, **kwargs):
        order = retrieve_order(request.user, kwargs['pk'])
        serializer = RetrieveOrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            update_order(serializer, request.user, kwargs['pk'])
            return Response({'Order successfully updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = Order.objects.filter(custom_user=request.user)
        serializer = RetrieveOrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # think if it is needed
    def destroy(self, request, *args, **kwargs):
        Order.objects.filter(custom_user=request.user, ordered=True).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
