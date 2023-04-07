from django.utils import timezone

from django.db import models

# models
from users.models import User

# Create your models here.
class Token(models.Model):
    access_token = models.TextField()
    refresh_token = models.TextField()
    access_token_expiration = models.DateTimeField()
    refresh_token_expiration = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self)->str:
        return f"Token user {self.user.phone_number}"
    