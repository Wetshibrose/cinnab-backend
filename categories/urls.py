from django.urls import path

# views
from .views import (
    RetrieveCategoriesAPIView,
    RetrieveCategoryAPIView,
    CreateCategoryAPIView,
    EditCategoryAPIView,
    DeleteCategoryAPIView,
)

urlpatterns = [
    path("", RetrieveCategoriesAPIView.as_view(), name="categories"),
    path("new", CreateCategoryAPIView.as_view(), name="new_category"),
    path("<str:category_id>", RetrieveCategoryAPIView.as_view(), name="category"),
    path("edit/<str:category_id>", EditCategoryAPIView.as_view(), name="edit_category"),
    path("delete/<str:category_id>", DeleteCategoryAPIView.as_view(), name="delete_category"),
]