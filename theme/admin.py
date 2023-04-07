from django.contrib import admin

# models
from .models import Theme

class ThemeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Theme, ThemeAdmin)
