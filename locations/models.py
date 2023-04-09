from uuid import uuid4

from django.contrib.gis.db import models
from django.utils import timezone

# models
from users.models import User

class UserLocation(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    address_line_1 = models.CharField(max_length=255, default="")
    address_line_2 = models.CharField(max_length=255, blank=True, default="")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20, blank=True, default="")
    location = models.PointField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.address_line_1}, {self.city}, {self.country}'