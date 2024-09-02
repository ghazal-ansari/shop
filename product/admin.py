from django.contrib import admin
from .models import ProductInfo


# Register your models here.

admin.sites.AdminSite.site_header = "پنل مدیریت سایت"
admin.sites.AdminSite.site_title = "پنل مدیریت سایت"
admin.sites.AdminSite.index_title = "پنل مدیریت"
# Register your models here.
admin.site.register(ProductInfo)