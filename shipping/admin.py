from django.contrib import admin

# models
from .models import ShippingMethod

class ShippingMethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShippingMethod, ShippingMethodAdmin)
