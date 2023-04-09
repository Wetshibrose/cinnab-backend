from django.contrib import admin

# models
from .models import WishList

class WishListAdmin(admin.ModelAdmin):
    pass

admin.site.register(WishList, WishListAdmin)
