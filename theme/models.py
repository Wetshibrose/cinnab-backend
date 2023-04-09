from uuid import uuid4

from django.contrib.gis.db import models
from django.utils import timezone


class Theme(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    primary_color = models.CharField(max_length=200, default="", blank="")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)


    def __str__(self)->str:
        return f"primary color {self.primary_color}"