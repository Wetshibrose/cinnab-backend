from django.urls import path

from .views import CustomTokenObtainPairView, LoginAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("token", CustomTokenObtainPairView.as_view(), name="obtain_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("login", LoginAPIView.as_view(), name="login")
]