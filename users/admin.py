from django.contrib import admin

# models
from .models import User, ProfilePicture, GenderType

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)

class ProfilePictureAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProfilePicture, ProfilePictureAdmin)

class GenderTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(GenderType, GenderTypeAdmin)