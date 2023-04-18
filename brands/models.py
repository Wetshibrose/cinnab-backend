from uuid import uuid4

from django.contrib.gis.db import models
from django.utils import timezone

# models
from businesses.models import Business


class Brand(models.Model):
    class Meta:
        default_related_name = "brands"
        indexes = [
            models.Index(fields=["id", "name"])
        ]
        ordering = ["name"]
        verbose_name = "brand"
        verbose_name_plural = "brands"

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    business = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)


class BrandLogo(models.Model):
    class Meta:
        default_related_name = "brandlogos"
        indexes = [
            models.Index(fields=["id","is_deleted"])
        ]
        ordering = ["-date_created"]
        verbose_name = "brand logo"
        verbose_name_plural = "brand logos"

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    url = models.URLField(verbose_name="url image", blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)