from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProfileView, AddressView

urlpatterns = [
    path('', ProfileView.as_view()),
]

router = DefaultRouter()

router.register(r'address', AddressView, basename="OrderItemViewSet")

urlpatterns += router.urls
