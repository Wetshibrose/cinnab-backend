from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("authentication/", include("authentication.urls")),
    path("categories/", include("categories.urls")),
    path("users/", include("users.urls")),
    path("theme/", include("theme.urls")),
]
