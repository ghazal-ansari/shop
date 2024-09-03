from django.shortcuts import render
from .models import ProductInfo, Cart, CartItem, Category
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    product_tmp = ProductInfo.objects.all()
    products = ProductSerializer(product_tmp, many = True)
    if request.method == "POST":
        data = request.POST.get("product")
        print("*******",data)
        pr = request.session.get("selected")
        if pr is None:
            pr=[]
        pr.append(data)
        request.session["selected"] = pr
        print(pr)
    
    rt = render(request=request,template_name="index.html",context={"products":products.data})
    # rt.set_cookie("selected",pr)
    return rt




def add_to_cart(request, product_id):
    product = get_object_or_404(ProductInfo, id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        print("ok user 1")
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            print("2")
        cart = Cart.objects.create(session_key=session_key)
        print("created")

    cart_item = CartItem.objects.create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        print("created")
    return redirect('products:cart')



def view_cart(request):
    if request.method == "POST":
        data = request.POST.get("product")
        pr = request.session.get("selected")
        pr.remove(data)
        request.session["selected"] = pr
    sessions = request.session.get('selected',[])
    products = ProductInfo.objects.filter(id__in=sessions)
    total_price= sum([item.price for item in products])
    return render(request, template_name="cart.html",context=
                  {"products":products,"total_price":total_price})
    
def indexF(request):
    return render(request, 'indexF.html')

def shop(request):
    return render(request, 'shop.html')

def contact(request):
    return render(request, 'contact.html')

def sign_up(request):
    return render(request, 'sign-up.html')