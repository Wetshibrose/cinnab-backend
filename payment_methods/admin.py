from django.contrib import admin

# models 
from .models import PaymentMethod

class PaymentMethodAdmin(admin.ModelAdmin):
    pass

admin.site.register(PaymentMethod, PaymentMethodAdmin)

