from uuid import uuid4
# django
from django.contrib.gis.db import models
from django.utils import timezone

class Currency(models.Model):
    class Meta:
        verbose_name_plural = "currencies"
        
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    code = models.CharField(max_length=200, default="USD")
    conversion_rate = models.FloatField(default=1.0,)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)