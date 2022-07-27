from rest_framework import serializers

from .models import Book


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id",
                  "title",
                  "pages_number",
                  "publishment_year",
                  "description",
                  "genre",
                  "price",
                  "discount_percentage",
                  "image",
                  "author")
