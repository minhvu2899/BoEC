from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import redirect, render
from django.views import View
from cart.models import *
from .models import *
from user.models import *



# Create your views here.
class AddOrder(View):
    def post(self,request):
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cartItem = cart.cartitem_set.all()
            total=request.POST.get('total')
            shipping_id =request.POST.get('shipping_id')
            payment_id =request.POST.get('payment_id')
            ship= Shipping.objects.get(pk = shipping_id)
            pay =Payment.objects.get(pk = payment_id)
            address_user=Address.objects.get(user= request.user,default=True)
            shipping_address = address_user.street +',' +  address_user.apartment_number+','+ address_user.district+ ','+address_user.city
            order =Order.objects.create(user=request.user,cart= cart,shipping_address=shipping_address,ship=ship, paymentMethod=pay,total=total)
            for item in cartItem:
                OrderDetail.objects.create(order= order, product= item.item,product_name=item.title, image =item.thumbnail,quantity= item.quantity,price=item.item.sale_price)
                # HttpResponse(item.item.sale_price)
            cart.cartitem_set.all().delete()    
            return HttpResponse(1)
class GetRatingOrder(View):
    def get(self,request):
        if request.user.is_authenticated:
            id= request.POST.get('id')
            order =Order.objects.get(pk=18, user=request.user)   
            o = list(OrderDetail.objects.filter(is_rating=True, order=order).values())
         
            comment =list(Comment.objects.filter(order_id=18).values())
        return JsonResponse({"o":o,"c":comment},safe=False)
     
    def post(self,request):
        if request.user.is_authenticated:
            id= request.POST.get('id')
            order =Order.objects.get(pk=id, user=request.user)   
            o = list(OrderDetail.objects.filter(is_rating=True, order=order).values())
         
            comment =list(Comment.objects.filter(order_id=id).values())
        return JsonResponse({"o":o,"c":comment},safe=False)


class OrderManage(View):
    def get(seft,request):
        orders =Order.objects.all()
        context={}
        context['orders']= orders
        return render(request,"order/manage.html",context)
    def post(seft,request):
        orders =Order.objects.all()
        context={}
        context['orders']= orders
        return render(request,"order/manage.html",context)
class OrderStatus(View):
    def get(seft,request,type):
        status =type
        if status==0:
            order = Order.objects.all()
            count = order.count()
        else:
            order = Order.objects.filter(status=status)
            count = order.count()
        
       
        context={}
        context['orders']=order
        context['active'] =status    
        context['count']=count
       
        return render(request,"order/manage.html",context)
    def post(seft,request,type):
        status =type
        count={}
        if status==0:
            order = Order.objects.all()
            count = order.count()
        else:
            order = Order.objects.filter(status=status)
            count = order.count()
        

        context={}
        context['orders']=order
        context['active'] =status    
        context['count']=count
        return render(request,"order/manage.html",context)
        # return JsonResponse(order,safe=False)
class UpdateStatus(View):
    def get(seft,request,order,type):
        Order.objects.filter()
        return HttpResponse(1)
    def post(seft,request):
        order = request.POST.get('orderid')
        type = request.POST.get('type')
        type1= int(type)+1
        Order.objects.filter(pk=order,status=int(type)).update(status=type1)
        # return HttpResponse(order)
        return HttpResponseRedirect(seft.request.META.get('HTTP_REFERER'))
      