from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .forms import LoginForm , SignUpForm
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
def dashboard(request):
    return render(request, 'dashboard.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        

        user = User.objects.create(
            name=name,
            surname=surname,
            username=username,
            email=email
        )
        user.set_password(password1)
        user.save()

        login(request, user)
        return redirect('products:indexF')
    return render(request, 'usign-up.html')


    
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products:indexF')
        else:
            return render(request, 'usign-up.html', {'error': "Invalid username or password"})

    return render(request, 'usign-up.html')


#----------------------------------------------------------------------------------
           


def indexF(request):
    return render(request, 'indexF.html')

def shop(request):
    return render(request, 'shop.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return redirect('product/cart.html')


    
# def sign_up(request):
#     print("wwwwwwwww")
#     return render(request, 'usign-up.html')