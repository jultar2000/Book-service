from django.urls import path
from .views import ListCreateItemView, UpdateItemView

urlpatterns = [
    path('', ListCreateItemView.as_view()),
    path(r'<int:id>/', UpdateItemView.as_view())
]
