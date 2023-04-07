from django.contrib import admin

# models
from .models import Token

class TokenAdmin(admin.ModelAdmin):
    pass

admin.site.register(Token, TokenAdmin)
