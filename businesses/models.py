from uuid import uuid4
# django
from django.contrib.gis.db import models
from django.utils import timezone

# models
from users.models import User
from locations.models import UserLocation


class Business(models.Model):
    class Meta:
        default_related_name = "businesses"
        indexes = [
            models.Index(fields=["id", "name", "user"]),
        ]
        ordering = ["name",]
        verbose_name = "business"
        verbose_name_plural = "businesses"

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    website = models.URLField(null=True)
    is_verified = models.BooleanField(default=False)
    address = models.ForeignKey(UserLocation, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BusinessLogo(models.Model):
    class Meta:
        # db_table = "p_images" env file
        default_related_name = "businesslogos"
        indexes = [
            models.Index(fields=["id","is_deleted"]),
        ]
        verbose_name = "business logo"
        verbose_name_plural = "business logos"
        ordering = ["-date_created",]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    url = models.URLField(verbose_name="url image", blank=True, null=True)
    business = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True,)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)

