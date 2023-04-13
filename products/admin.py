from django.contrib import admin

# models
from .models import (
    Product, 
    ProductImage,
    ProductVariant
)

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
