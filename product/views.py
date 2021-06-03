from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from .models import Category, Product
from .forms import FormCreateProduct,UploadFileForm
import json
from django.core.paginator import Paginator
from django.core.serializers import serialize
import pandas as pd
from order.models import OrderDetail
# Create your views here.
class ProductView(View):
    def get(seft,request):
        context={}
       
        
        context['categorys'] = Category.objects.all()
        product_list = Product.objects.all()
        paginator = Paginator(product_list, 12) # Show 25 contacts per page.
      
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        for item in page_obj:
            item.sale_price ="₫{:,.0f}".format(item.sale_price)
        context['page_obj']= page_obj
        return render(request, 'product/product.html', context)

    
class CategoryView(View):
    def get(seft,request,slug):
        context={}
        c = Category.objects.get(slug=slug)
        product_list=  c.product_set.all()
        context['categorys'] = Category.objects.all()
        paginator = Paginator(product_list, 12) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for item in page_obj:
            item.sale_price ="₫{:,.0f}".format(item.sale_price)
        context['page_obj']= page_obj
        return render(request, 'product/product.html', context)
    def post(seft,request):
        context={}
        a=request.POST['search']
        context['categorys'] = Category.objects.all()
        return render(request, "product/product.html",context)
class DetailView(View):
    def get(seft,request,id):
        context={}
        context['product_id']=id
        product=   Product.objects.get(id=id)
        product.sale_price ="₫{:,.0f}".format(product.sale_price)
        context['list'] = product
        comments = product.comment_set.all()
        context['comments']=comments
        return render(request, "product/detail.html",context)
  
class SearchProduct(View):
    def get(self, request):
        order = OrderDetail.objects.all()
        for o in order:
            o.product_name= o.product.title
            o.image= o.product.thumbnail
            o.save()
        return HttpResponse(1)
    def post(seft,request):   
        text_search = request.POST.get('text_search') 
        context={}
        context['categorys'] = Category.objects.all()
        product= Product.objects.filter(title__icontains=text_search)
        paginator = Paginator(product, 12) # Show 25 contacts per page.
       
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
  
        for item in page_obj:
            item.sale_price ="₫{:,.0f}".format(item.sale_price)
        context['page_obj']= page_obj
        return render(request, 'product/product.html', context)
       
  
