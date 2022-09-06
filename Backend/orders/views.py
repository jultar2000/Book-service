from rest_framework.generics import DestroyAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ViewSet

from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderSerializer
from .services import add_order_item_to_cart, \
    retrieve_order_item, retrieve_order, update_order_item, update_order
from rest_framework.response import Response
from rest_framework import status


# prevent update from user that is not the owner of the specific order
class OrderItemViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        add_order_item_to_cart(request)
        return Response('Item added to cart', status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        update_order_item(request, pk)
        return Response('Item updated', status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        order_item = retrieve_order_item(request.user, pk=pk)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # why when pk not specified all objects are deleted?
    def destroy(self, request, pk=None):
        retrieve_order_item(request.user, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        queryset = OrderItem.objects.filter(custom_user=request.user)
        serializer = OrderItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# TODO >> prevent from saving and updating objects not owned by authenticated user
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
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        update_order(request, kwargs['pk'])
        return Response('Order updated', status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = Order.objects.filter(custom_user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # think if it is needed
    def destroy(self, request, *args, **kwargs):
        Order.objects.filter(custom_user=request.user, ordered=True).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
