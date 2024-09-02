from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'api'

urlpatterns = [
    path('user/get-user',get_user,name='get_user'),
    path('product/get-product',ManageProduct.as_view(),name='get_product'),
    path('product/create-product',func_product,name='create_product'),
    ]
