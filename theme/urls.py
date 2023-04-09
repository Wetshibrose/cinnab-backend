from django.urls import path

# views
from .views import (
    RetrieveThemesAPIView,
    RetrieveThemeAPIView,
    CreateUserAPIView,
    EditUserAPIView,
    DeleteUserAPIView
)

app_name = "theme"

urlpatterns = [
    path("", RetrieveThemesAPIView.as_view(), name="themes"),
    path("newTheme", CreateUserAPIView.as_view(), name="new_theme"),
    path("<str:theme_id>", RetrieveThemeAPIView.as_view(), name="theme"),
    path("editTheme/<str:theme_id>", EditUserAPIView.as_view(), name="edit_theme"),
    path("deleteTheme/<str:theme_id>", DeleteUserAPIView.as_view(), name="themes"),
]