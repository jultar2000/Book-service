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
        order_item = OrderItem.objects.get(book=book)
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
