from django.db import IntegrityError

from books.models import Book
from utils.exceptionhandler import CustomApiException
from orders.models import OrderItem


def add_order_item_to_cart(request):
    data = request.data

    try:
        order_item = OrderItem.objects.create(
            book=Book.objects.get(pk=data.get('book')),
            quantity=data.get('quantity'),
            book_language=data.get('book_language'),
            book_cover=data.get('book_cover'))
    except IntegrityError as ex:
        raise CustomApiException(ex.__cause__.__str__(), 400)

    return order_item
