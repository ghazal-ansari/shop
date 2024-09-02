from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'users'

urlpatterns = [
    path('', index,name='index'),
    path('dashboard/',dashboard_view,name= 'dashboard'),
    path('login/',otp_login,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup',signup,name='signup'),
    path('login/verify',verify_code,name='verify'),
]
