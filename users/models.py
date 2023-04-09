from uuid import uuid4, UUID
from django.contrib.gis.db import models

from django.conf import settings
from django.utils.translation import gettext_lazy as _

# imports for abstract user model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# signal module imports
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete, post_save

# time module
from django.utils import timezone

# models


# custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **kwargs):
        if not phone_number:
            raise ValueError("The Phone Number field must be set")
        
        user = self.model(
            phone_number=phone_number,
            **kwargs
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Super User should be staff member")
                
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Super User should be superuser")

        return self.create_user(phone_number=phone_number, password=password, **kwargs)

class GenderType(models.Model):
    class Meta:
        verbose_name_plural = "genders"
        ordering = ["name"]
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)

    def __str__(self)->str:
        return self.name
    
    

class User(AbstractUser):
    class Meta:
        verbose_name_plural = "users"
        ordering = ["email"]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    government_id = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(auto_created=True, blank=True, null=True)
    gender = models.ForeignKey(GenderType, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    objects=CustomUserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    @property
    def is_admin(self):
        return self.is_staff

    @property
    def is_vendor(self):
        pass

    def __str__(self):
        return self.phone_number

class ProfilePicture(models.Model):
    class Meta:
        verbose_name_plural = "profile pictures"
        ordering = ["-date_created"]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    url = models.URLField(verbose_name="url photo", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)

    