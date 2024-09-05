from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'users'

urlpatterns = [
    path('', index,name='index'),
    path('dashboard/',dashboard_view,name= 'dashboard'),
    path('login/',sign_up,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('login/verify',verify_code,name='verify'),

    # path('home/', indexF, name='indexF'),
    # path('shop/', shop, name='shop'),  # Shop page
    # path('cart/', cart, name='cart'),  # Cart page
    # path('contact/', contact, name='contact'),  # Contact Us page
    # path('sign-up/', sign_up, name='sign-up'),  # Sign Up (Sign In) page
]
