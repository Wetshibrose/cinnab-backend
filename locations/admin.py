from django.contrib import admin

# models
from .models import UserLocation

class UserLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserLocation, UserLocationAdmin)