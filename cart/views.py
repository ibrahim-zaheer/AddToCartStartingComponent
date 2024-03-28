from django.shortcuts import render,redirect
from .models import Cartitem,Products
from django.http import HttpResponse
# Create your views here.


def product_list(request):
    productLists = Products.objects.all()
    return render(request,'index.html',{'products':productLists})


def view_cart(request):
    cartData = Cartitem.objects.filter(user = request.user)
    total_price = sum(item.products.price*item.quantity for item in cartData)
    return render(request,"cart.html",{'cart_items':cartData,'total_price':total_price})


# def add_to_cart(request,product_id):
#     product = Products.objects.filter(id = product_id)
#     cart_item,created = Cartitem.objects.get_or_create(product = product_id,user = request.user)
#     cart_item.quantity+=1
#     cart_item.save()
#     return redirect("cart:view_cart")
def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)  # Retrieve single Product instance
    cart_item, created = Cartitem.objects.get_or_create(products=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart:view_cart")

def remove_from_cart(request,product_id):
    product = Cartitem.objects.get(id = product_id)
    product.delete()
    product.save()
    return redirect("cart:view_cart")

def home(request):
    return HttpResponse('Hello, World!')