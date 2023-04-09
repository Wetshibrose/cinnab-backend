from uuid import uuid4
# django
from django.contrib.gis.db import models
from django.utils import timezone

class PaymentMethod(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, default="Cash")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)