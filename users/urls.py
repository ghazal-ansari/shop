from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('', indexF, name='index'),  # Home page
    path('home/', indexF, name='indexF'),
    path('cart/', cart, name='cart'),  # Cart page
    path('shop/', shop, name='shop'),  # Shop page
    path('contact/', contact, name='contact'),  # Contact Us page
    path('sign-up/', sign_up, name='sign-up'),  # Sign Up (Sign In) page
]
