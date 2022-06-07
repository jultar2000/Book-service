from django.urls import path
from accounts.views import SignUpView, ActivateAccount
from .views import CustomTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>', ActivateAccount.as_view(), name='activate'),
    path('sign-in/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
