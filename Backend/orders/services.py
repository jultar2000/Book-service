from django.db import IntegrityError

from books.models import Book
from utils.exceptionhandler import CustomApiException
from orders.models import OrderItem, Order


def add_order_item_to_cart(validated_data, user):
    try:
        order, created = Order.objects.get_or_create(
            custom_user=user,
            ordered=False)
    except IntegrityError as ex:
        raise CustomApiException(ex.__cause__.__str__(), 400)

    try:
        order_item = OrderItem.objects.get(custom_user=user, book=validated_data.get('book').id)
        order_item.quantity += 1
        order_item.save()
    except OrderItem.DoesNotExist:
        try:
            order_item = OrderItem.objects.create(
                order=order,
                custom_user=user,
                book=Book.objects.get(pk=validated_data.get('book').id),
                quantity=validated_data.get('quantity'),
                book_language=validated_data.get('book_language'),
                book_cover=validated_data.get('book_cover'))
        except IntegrityError as ex:
            raise CustomApiException(ex.__cause__.__str__(), 400)

    return order_item


def retrieve_order_item(user, pk):
    try:
        return OrderItem.objects.get(custom_user=user, pk=pk)
    except OrderItem.DoesNotExist:
        raise CustomApiException("Item does not exist", 400)


# TODO >> prevent from saving an empty strings
def update_order_item(serializer, user, pk):
    try:
        order_item = OrderItem.objects.get(custom_user=user, pk=pk)
    except OrderItem.DoesNotExist:
        raise CustomApiException("Item does not exist", 400)
    serializer.update(order_item, serializer.validated_data)


def retrieve_order(user, pk):
    try:
        return Order.objects.get(custom_user=user, pk=pk)
    except Order.DoesNotExist:
        raise CustomApiException("Order does not exist", 400)


def update_order(serializer, user, pk):
    try:
        order = Order.objects.get(custom_user=user, pk=pk)
    except Order.DoesNotExist:
        raise CustomApiException("Order does not exist", 400)
    serializer.update(order, serializer.validated_data)
