from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .forms import LoginForm , SignUpForm,OtpForm,VerifyCode
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from random import randint
import requests
from shop import settings
from django.contrib import messages
from kavenegar import *



# Create your views here.

#------------------------------------------------------------------------------------
# @login_required
# def dashboard_view(request):
#     return render(request=request,template_name='user/dashboard.html')

# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('users:home')  
#     else:
#         form = SignUpForm()

#     return render(request, 'users/sign-up.html', {'form': form})

    
# def signin(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('users:home')  
#             else:
#                 error_message = "Invalid username or password."
#                 return render(request, 'user/signin.html', {'form': form, 'error': error_message})
#     else:
#         form = LoginForm()

#     return render(request, 'users/signin.html', {'form': form})

#----------------------------------------------------------------------------------
           


def indexF(request):
    return render(request, 'indexF.html')

def shop(request):
    return render(request, 'shop.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return redirect('product/cart.html')
    
def sign_up(request):
    print("wwwwwwwww")
    return render(request, 'usign-up.html')