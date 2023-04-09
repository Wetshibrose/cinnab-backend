from uuid import uuid4
# django
from django.contrib.gis.db import models
from django.utils import timezone

# models
from users.models import User
class WishList(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, default="wishlist")
    notes = models.TextField(blank=True)
    # product models
    # product variant models
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now,)
    updated_at = models.DateTimeField(null=True)

    @property
    def total_price(self)->float:
        pass

    @property
    def total_discount(self)->float:
        pass

    @property
    def total_no_products(self)->int:
        pass

    def __str__(self)->str:
        return f"Wishlist {self.name}"
    