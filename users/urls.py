from django.urls import path

# views
from .views import (
    RetrieveUsersAPIView, RetrieveUserAPIView, CreateUserAPIView, EditUserAPIView, DeleteUserAPIView ,
    )

app_name = "users"

urlpatterns = [
    path("", RetrieveUsersAPIView.as_view(), name="users",),
    path("<str:user_id>", RetrieveUserAPIView.as_view(), name="user"),
    path("newUser", CreateUserAPIView.as_view(), name="new_user",),
    path("editUser/<str:user_id>", EditUserAPIView.as_view(), name="edit_user",),
    path("deleteUser/<str:user_id>", DeleteUserAPIView.as_view(), name="delete_user",),
]

