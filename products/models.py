from uuid import uuid4

from django.contrib.gis.db import models
from django.utils import timezone

class Product(models.Model):
    class Meta:
        # db_table = "p_products" env file
        default_related_name = "products"
        indexes = [
            models.Index(fields=["name", "rating",]),
            # models.Index(fields=["category", "brands"]),
        ]
        ordering = ["name"]
        verbose_name = "product"
        verbose_name_plural = "products"

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
    color = models.CharField(max_length=255, null=True)
    # brands = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    # tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True)
    # business = models.ForeignKey(Business, on_delete=models.SET_NULL)
    # sku = models.ForeignKey(Unit, null=True)
    is_tracking = models.BooleanField(default=True)
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

    @property
    def product_images(self)->list[str]|list:
        images:list = ProductImage.objects.filter(product__id=self.id)
        if images.exists():
            return images
        return []


class ProductImage(models.Model):
    class Meta:
        # db_table = "p_images" env file
        indexes = [
            models.Index(fields=["id","is_deleted"]),
        ]
        default_related_name = "product_images"
        verbose_name = "product image"
        verbose_name_plural = "product images"
        ordering = ["-date_created"]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    url = models.URLField(verbose_name="url image", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)


class ProductVariant(models.Model):
    class Meta:
        # db_table = "p_variant" env file
        indexes = [
            models.Index(fields=["name", "rating"]),
            # models.Index(fields=["category", ])
        ]
        default_related_name = "product_variants"
        verbose_name = "product variant"
        verbose_name_plural = "product variants"
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
    color = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    # tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True)
    # business = models.ForeignKey(Business, on_delete=models.SET_NULL)
    # sku = models.ForeignKey(Unit, null=True)
    is_tracking = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    on_offer = models.BooleanField(default=False)
    featured_until = models.DateField(null=True)
    mnf_date = models.DateField(verbose_name="Manufactured date", null=True)
    exp_date = models.DateField(verbose_name="Expiry date", null=True)
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True)

    def __str__(self)->str:
        return f"{self.name} is a variant of {self.product.name}"