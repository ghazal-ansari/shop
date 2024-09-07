from django.urls import path
from .views import index, view_cart, shop, contact, add_to_cart, indexF, remove,remove_all, product_list
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('home/', indexF, name='indexF'),
    path('cart/', view_cart, name='cart'),  # Cart page
    path('shop/', shop, name='shop'),  # Shop page
    path('contact/', contact, name='contact'),  # Contact Us page
    #path('sign-up/', sign_up, name='sign-up'),  # Sign Up (Sign In) page
    path('remove_product/', remove, name='remove'),
    path('remove_all/', remove_all),
    path('category/<str:category>/', product_list, name='product_list_by_category'),
    path('', product_list, name='product_list_'),
]
