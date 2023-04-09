from uuid import uuid4

from django.contrib.gis.db import models
from django.utils import timezone

class Product(models.Model):
    class Meta:
        verbose_name_plural = "products"
        ordering = ["name"]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock_quantity = models.IntegerField(null=True)
    barcode = models.CharField(max_length=255, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    # tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True)
    # business = models.ForeignKey(Business, on_delete=models.SET_NULL)
    # sku = models.ForeignKey(Unit, null=True)
    is_active = models.BooleanField(default=True)
    on_offer = models.BooleanField(default=False)
    featured_until = models.DateField(null=True)
    mnf_date = models.DateField(verbose_name="Manufactured date", null=True)
    exp_date = models.DateField(verbose_name="Expiry date", null=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)

    @property
    def profit_per_product(self)->float:
        b_price:float = 0
        discount = 0
        if self.buying_price is not None:
            b_price = self.buying_price

        if self.discount_price:
            discount = self.discount_price

        profit:float = (self.selling_price - b_price) - discount
        return profit
    
    @property
    def days_before_expiry(self):
        pass

    @property
    def has_stock(self)->bool:
        return self.stock_quantity>0
    
    @property
    def num_variants(self)->int:
        pass

    @property
    def num_of_reviews(self)->int:
        pass


class ProductImage(models.Model):
    class Meta:
        verbose_name_plural = "product images"
        ordering = ["-date_created"]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    url = models.URLField(verbose_name="url image", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)


class ProductVariant(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    