from django.contrib import admin
# models
from .models import UserSetting

class UserSettingAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserSetting, UserSettingAdmin)

