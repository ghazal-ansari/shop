from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User




# Create your views here.

#------------------------------------------------------------------------------------
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            'user': user
        }
        return render(request, 'dashboard.html', context)
    else:
        return render(request, 'dashboard.html', {'error': "You must be logged in to access the dashboard."})


def user_logout(request):
    logout(request)
    return render(request, 'indexF.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        

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

        print(username, password, "cd")
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('products:indexF')
        else:
            return render(request, 'dashboard.html', {'error': "Invalid username or password"})

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