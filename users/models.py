from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "AD","Admin"
        SHOP_ADMIN = "SH","ShopAdmin"
        CUSTOMER = "CU","Customer"
    national_code = models.CharField(max_length =50,null=True,blank=True,verbose_name ="کد ملی")
    phone = models.CharField(max_length =50,null=True,blank=True,verbose_name ="شماره تماس")
    address= models.TextField(null=True,blank=True,verbose_name="ادرس")
    last_ip = models.GenericIPAddressField(null = True,blank = True,verbose_name = 'آخرین ادرس آی پی')
    role = models.CharField(max_length = 2,choices = Role.choices,default = Role.CUSTOMER,verbose_name = 'نقش')