from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('accounts.urls'), name='accounts'),
    path('api/v1/profiles/', include('profiles.urls'), name='profiles'),
    path('api/v1/authors/', include('authors.urls'), name='authors'),
    path('api/v1/books/', include('books.urls'), name='books'),
    path('api/v1/orders/', include('orders.urls'), name='orders'),
]
