from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class ProductInfo(models.Model):
    name = models.CharField(max_length=70, verbose_name="نام ")
    description = models.TextField(verbose_name="توضیحات")
    category = models.TextField(verbose_name='دسته بندی', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    price = models.BigIntegerField(verbose_name='قیمت', default=0)
    image = models.ImageField(upload_to='images/', verbose_name="تصویر", blank=True, null=True)  

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True, default='default_session_key')  # Unique session identifier
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} (Session {self.session_key})"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

