from uuid import uuid4
# django
from django.contrib.gis.db import models
from django.utils import timezone

# models
from currencies.models import Currency
from languages.models import Language
from payment_methods.models import PaymentMethod
from theme.models import Theme
from users.models import User

class UserSetting(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    is_notified = models.BooleanField(default=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)



