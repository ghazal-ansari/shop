from django.urls import path
from .views import index, view_cart, shop, contact, sign_up, add_to_cart, indexF
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('home/', indexF, name='indexF'),
    path('cart/', view_cart, name='cart'),  # Cart page
    path('shop/', shop, name='shop'),  # Shop page
    path('contact/', contact, name='contact'),  # Contact Us page
    path('sign-up/', sign_up, name='sign-up'),  # Sign Up (Sign In) page
]
