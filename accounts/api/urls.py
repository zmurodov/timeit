from django.urls import path

from .views import UserListAPIView, UserDetailAPIView, UserRegisterAPIView

app_name = 'accounts-api'

urlpatterns = [
    path("accounts/", UserListAPIView.as_view(), name='api-user-list'),
    path("accounts/register/", UserRegisterAPIView.as_view(), name='api-user-register'),
    path('accounts/<int:pk>/', UserDetailAPIView.as_view(), name='api-user-details'),
]
