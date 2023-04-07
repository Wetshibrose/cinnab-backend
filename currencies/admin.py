from django.contrib import admin

# models
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Currency, CurrencyAdmin)
