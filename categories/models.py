from uuid import uuid4
# django
from django.contrib.gis.db import models
from django.utils import timezone

class Category(models.Model):
    class Meta:
        default_related_name = "categories"
        indexes = [
            models.Index(fields=["id", "parent"]),
        ]
        ordering = ["name"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, default="", blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    related_categories = models.ManyToManyField('self', blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return f"Category {self.name}"