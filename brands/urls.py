from django.urls import path

# views
from .views import (
    RetrieveBrandsAPIView,
    RetrieveBrandAPIView,
    CreateBrandAPIView,
    EditBrandAPIView,
    DeleteBrandAPIView
)

urlpatterns = [
    path("", RetrieveBrandsAPIView.as_view(), name="brands"),
    path("newBrand", CreateBrandAPIView.as_view(), name="new_brand"),
    path("<str:brand_id>/", RetrieveBrandAPIView.as_view(), name="brand"),
    path("editBrand/<str:brand_id>/", EditBrandAPIView.as_view(), name="edit_brand"),
    path("deleteBrand/<str:brand_id>/", DeleteBrandAPIView.as_view(), name="delete_brand"),
]