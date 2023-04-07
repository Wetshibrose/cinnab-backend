from django.contrib import admin

# models
from .models import Language

class LanguageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Language, LanguageAdmin)
