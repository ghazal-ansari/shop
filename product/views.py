from django.shortcuts import render
from .models import ProductInfo, Cart, CartItem
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
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    print(cart_item, "zzzz")
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

    products_id = Cart.objects.get(session_key = request.session.session_key)
    products_selected = CartItem.objects.values_list('product_id').filter(cart_id=products_id.id)
    products =  ProductInfo.objects.filter(id__in=products_selected)
    print(products_id, "kkkkkkkkkkk", products_selected, products)
    total_price= sum([item.price for item in products])
    return render(request, template_name="cart.html",context=
                  {"products":products,"total_price":total_price})
    
def indexF(request):
    return render(request, 'indexF.html')

def shop(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def sign_up(request):
    return render(request, 'sign-up.html')