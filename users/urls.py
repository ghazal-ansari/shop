from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', indexF, name='index'),  # Home page
    path('home/', indexF, name='indexF'), #Home Page
    path('cart/', cart, name='cart'),  # Cart page
    path('shop/', shop, name='shop'),  # Shop page
    path('contact/', contact, name='contact'),  # Contact Us page
    path('sign-up/', signup, name='sign-up'),  # Sign Up (Sign In) page
    path('sign-uin/', signin, name='sign-in'),  # Sign Up (Sign In) page
    path('dashboard/', dashboard, name='dashboard'), #Dashboard Page
    path('logout/', user_logout, name='logout'),  #Log Out

]
