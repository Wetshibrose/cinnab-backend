from uuid import uuid4

from django.contrib.gis.db import models
from django.utils import timezone

class Language(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=5, default="EN")
    long_name = models.CharField(max_length=100, default="EN (UNITED KINGDOM)")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)
