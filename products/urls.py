from django.urls import path

# views
from .views import (
    RetrieveProductsAPIView,
    RetrieveProductAPIView,
    CreateProductAPIView,
    EditProductAPIView,
    DeleteProductAPIView
)

urlpatterns = [
    path("", RetrieveProductsAPIView.as_view(), name="products"),
    path("new", CreateProductAPIView.as_view(), name="new_product"),
    path("<str:product_id>", RetrieveProductAPIView.as_view(), name="product"),
    path("edit/<str:product_id>", EditProductAPIView.as_view(), name="edit_product"),
    path("delete/<str:product_id>", DeleteProductAPIView.as_view(), name="delete_product"),
]