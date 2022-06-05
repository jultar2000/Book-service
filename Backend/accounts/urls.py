from django.urls import path
from .views import SignUpView, ActivateAccount, SignInView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>',
         ActivateAccount.as_view(), name='activate'),
    path('sign-in/', SignInView.as_view(), name='signin'),
]
