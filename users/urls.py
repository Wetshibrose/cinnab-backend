from django.urls import path

# views
from .views import (
    RetrieveUsersAPIView, 
    RetrieveUserAPIView, 
    CreateUserAPIView, 
    EditUserAPIView, 
    DeleteUserAPIView, 
    RetrieveGenderTypesAPIView,
    RetrieveGenderTypeAPIView,
    CreateGenderTypeAPIView
    )

app_name = "users"

urlpatterns = [
    path("", RetrieveUsersAPIView.as_view(), name="users",),
    path("newUser", CreateUserAPIView.as_view(), name="new_user",),
    path("<str:user_id>", RetrieveUserAPIView.as_view(), name="user"),
    path("editUser/<str:user_id>", EditUserAPIView.as_view(), name="edit_user",),
    path("deleteUser/<str:user_id>", DeleteUserAPIView.as_view(), name="delete_user",),
    path("genders/", RetrieveGenderTypesAPIView.as_view(), name="gender_types"),
    path("genders/newGender", CreateGenderTypeAPIView.as_view(), name="new_gender_type"),
    path("genders/<str:gender_id>", RetrieveGenderTypeAPIView.as_view(), name="gender_type"),
]

