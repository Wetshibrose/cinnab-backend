from uuid import uuid4
# django
from django.contrib.gis.db import models
from django.utils import timezone

class ShippingMethod(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, )
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self)->str:
        return f"Shipping method: {self.name}"