from django.db import IntegrityError

from books.models import Book
from utils.exceptionhandler import CustomApiException
from orders.models import OrderItem, Order


def add_order_item_to_cart(request):
    data = request.data
    user = request.user
    book = Book.objects.get(pk=data.get('book'))
    try:
        order, created = Order.objects.get_or_create(
            custom_user=user,
            ordered=False)
    except IntegrityError as ex:
        raise CustomApiException(ex.__cause__.__str__(), 400)

    try:
        order_item = OrderItem.objects.get(custom_user=user, book=book)
        order_item.quantity += 1
        order_item.save()
    except OrderItem.DoesNotExist:
        try:
            order_item = OrderItem.objects.create(
                order=order,
                custom_user=user,
                book=Book.objects.get(pk=data.get('book')),
                quantity=data.get('quantity'),
                book_language=data.get('book_language'),
                book_cover=data.get('book_cover'))
        except IntegrityError as ex:
            raise CustomApiException(ex.__cause__.__str__(), 400)

    return order_item


def retrieve_order_item(user, pk):
    try:
        return OrderItem.objects.get(custom_user=user, pk=pk)
    except OrderItem.DoesNotExist:
        raise CustomApiException("Item does not exist", 400)


# TODO >> prevent from saving an empty strings
# TODO >> handle exceptions
def update_order_item(request, pk):
    data = request.data
    try:
        OrderItem.objects.filter(pk=pk) \
            .update(quantity=data.get('quantity'),
                    book_cover=data.get('book_cover'),
                    book_language=data.get('book_language'))
    except Exception as e:
        raise CustomApiException(e.__cause__.__str__(), 400)


def retrieve_order(user, pk):
    try:
        return Order.objects.get(custom_user=user, pk=pk)
    except Order.DoesNotExist:
        raise CustomApiException("Order does not exist", 400)


def update_order(request, pk):
    data = request.data
    try:
        Order.objects.filter(pk=pk) \
            .update(order_date=data.get('order_date'),
                    ordered=data.get('ordered'),
                    status=data.get('status'),
                    shipping_address=data.get('shipping_address'),
                    billing_address=data.get('billing_address'))
    except Exception as e:
        raise CustomApiException(e.__cause__.__str__(), 400)
