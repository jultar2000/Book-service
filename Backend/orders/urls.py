from django.urls import path
from .views import OrderItemView

urlpatterns = [
    path('', OrderItemView.as_view())
]
