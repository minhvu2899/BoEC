from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import CartItem,Cart
from user.models import *
from product.models import *
from order.models import *
from django.views import View
# Create your views here.
class CartView(View):
    def get(seft,request):
        context={}
        if request.user.is_authenticated:
            cart =Cart.objects.filter(user=CustomerUser.objects.get(id=request.user.id))
            if not cart:
                cart =Cart.objects.create(user= request.user)
            else:
                cart=Cart.objects.get(user=CustomerUser.objects.get(id=request.user.id))
            if(cart):
                cartItems= cart.cartitem_set.all()
                if cartItems.count() ==0:
                    return render(request,"cart/cartEmpty.html")
                else:
                    total=0
                    for cart in cartItems:
                        cart.total= int(cart.quantity)*int(cart.item.sale_price)
                        total = total+ int(cart.quantity)*int(cart.item.sale_price)
                    context['list'] =cartItems 
                    context['total']= total
                    # return HttpResponse(cartItems[0].total)
                    return render(request, "cart/cart.html",context)
            else:
                return redirect('account:login')
class deleteItem(View):
    def post(self,request):
        item =request.POST.get('cartItem')
        CartItem.objects.get(pk=item).delete()
        return HttpResponse(1)
class AddCart(View):
    def post(seft,request):
        product_id = request.POST.get('product_id')
        product_number = request.POST.get('product_number')
        # return HttpResponse(product_number)
        if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            pro=Product.objects.get(id=product_id)    
           
            if(cart.count()==0):
                cart1=Cart.objects.create(user=request.user)
                CartItem.objects.create(cart= cart1,item= pro,quantity=product_number)
                return HttpResponse(cart)
            else:
                cart=Cart.objects.get(user=request.user)
                item= CartItem.objects.filter(item=pro,cart=cart)
                if item:
                    item= CartItem.objects.get(item=pro,cart=cart)
                    item.quantity = int(item.quantity) + int(product_number)
                    item.save()
                    return HttpResponse(item)
                else:
                    x= CartItem.objects.create(cart= cart,item= pro,quantity=product_number)
                    return HttpResponse(x)
        else:
            return HttpResponse("login")
            
class CheckoutView(View):
    def get(seft,request):
        context={}
        if request.user.is_authenticated:
            cart=Cart.objects.get(user=CustomerUser.objects.get(id=request.user.id))
            add= Address.objects.get(user= request.user, default=True)
            address= add.ToString()
            listAddresses = Address.objects.filter(user=request.user).all()
            for add in listAddresses:
                add.address=add.ToString()
            ship=Shipping.objects.all()
            context['ship']= ship
            payment = Payment.objects.all()
            context['payment']= payment
            context['listAddress'] = listAddresses
            if(cart):
                cartItems= cart.cartitem_set.all()
                total=0
                for cart in cartItems:
                    cart.total= int(cart.quantity)*int(cart.item.sale_price)
                    total = total+ int(cart.quantity)*int(cart.item.sale_price)
                context['list'] =cartItems 
                context['total']= total
                context['address']= address
            return render(request,"cart/checkout.html",context)

class UpdateCart(View):
    def post(self, request):
        if request.user.is_authenticated:
          
            quantity = request.POST.get('quantity')
            cart_id = request.POST.get('cart_id')
            cartItem = CartItem.objects.get(pk=cart_id)
            cartItem.quantity = quantity
            cartItem.save()
        return HttpResponse(quantity)
