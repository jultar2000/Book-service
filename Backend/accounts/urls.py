from django.urls import path
from .views import SignUpView, ActivateAccount

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('activate/slug:<uid64>/slug:<token>/', ActivateAccount.as_view(), name='activate')
    path('activate/(?P<uidb64>/(?P<token>',
         ActivateAccount.as_view(), name='activate'),
]
