from django.urls import path, include
from .views import OrderItemViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [

]

router = DefaultRouter()

router.register(r'items', OrderItemViewSet, basename="OrderItemViewSet")
router.register(r'', OrderViewSet, basename="OrderViewSet")

urlpatterns += router.urls
