from django.urls import path, include
from .views import OrderItemViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', OrderViewSet, basename="OrderViewSet")
router.register('items', OrderItemViewSet, basename="OrderItemViewSet")

urlpatterns = [
    path('', include(router.urls)),

]
