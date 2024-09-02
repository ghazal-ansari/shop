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

def index(request):
    request.session['admin2'] = "admin khers"
    res = HttpResponse(request,"Set Cookie")
    res.set_cookie("admin2","admin2 hastam")
    return res
    # return render(request=request,template_name='user/index.html')

@login_required
def dashboard_view(request):
    return render(request=request,template_name='user/dashboard.html')

def signup(request):
    if request.method =="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = True
            user.save()       
    form = SignUpForm()
    print(request.session.items())
    return render(request=request,template_name='user/signup.html',context={'form':form})

# def login_user(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request=request,username = cd['username'],password = cd['password'])
#             if user is None:
#                 return HttpResponse(content='نام کاربری یا رمز عبور اشتباه است')
#             else:
#                 login(request=request,user=user)
#                 return render(request=request,template_name='user/inde.html')
#         else:
#             pass
#     else:
#         form = LoginForm()
#     return render(request=request,template_name='user/login.html',context={'form':form})

# def logout_user(request):
#     try:
#         user = User.objects.get(id = request.user.id)
#     except User.DoesNotExist:
#         print('yrdsssss')
#         return redirect('users:login')
#     logout(request=request)
#     print('yrdsssss2')
#     return render(request=request,template_name='user/inde.html')



def send_otp(phone_number):
    code = randint(1000,9999)
    api_key = settings.API_KEY_SMS
    message = f'your code is {code}'
    # api = KavenegarAPI(api_key)
    # data= {
    #     "receptor": phone_number,
    #     "message":message
    # }
    # res = api.sms_send(data)
    # print("*",res)
    url = f"https://api.kavenegar.com/v1/{api_key}/sms/send.json"
    data= {
        "receptor": phone_number,
        "message":message,
        "sender":"200050066"
    }
    res = requests.post(url=url,data=data)
    print(code)
    return code


def otp_login(request):
    if request.method == "POST":
        form_data = OtpForm(request.POST)
        if form_data.is_valid():
            c_data = form_data.cleaned_data
            print(c_data)
            try:
                user  = User.objects.get(phone = c_data.get("phone"))
                code = send_otp(user.phone)
                request.session["code"] = code
                form = VerifyCode()
                return render(request=request,template_name='registration/verify.html',context={"form":form})
            except User.DoesNotExist:
                pass

    
    login_form = OtpForm()
    return render(request=request,template_name="registration/login.html",context={
        "form":login_form
    })


def verify_code(request):
    if request.method == "POST":
        form_data = VerifyCode(request.POST)
        if form_data.is_valid():
            c_data = form_data.cleaned_data
            print(c_data.get("code"))
            print(request.session.get("code"))
            print(type(c_data.get("code")))
            print(type(request.session.get("code")))
            if  str(request.session.get("code")) ==str(c_data.get("code")) :
                print("welcome")
            else:
                print("login fail")
    login_form = OtpForm()
    return render(request=request,template_name="registration/login.html",context={
        "form":login_form
    })        