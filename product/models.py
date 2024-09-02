from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class ProductInfo(models.Model):
    name = models.CharField(max_length=70, verbose_name="نام ")
    description = models.TextField(verbose_name="توضیحات")
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    modified = models.DateTimeField(auto_now=True, verbose_name='تاریخ اپدیت')
    price = models.BigIntegerField(verbose_name='قیمت', default=0)
    pr_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ تولید')
    exp_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انقضا")
    brand = models.CharField(max_length=50, null=True, blank=True, verbose_name="برند")
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

class Category(models.Model):
    name = models.CharField(max_length=70, verbose_name="نام دسته بندی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی‌ها'