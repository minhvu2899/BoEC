from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
from product.models import *
class HomeView(View):
    def get(seft,request):
        context={}
        product_list = Product.objects.all()
        paginator = Paginator(product_list, 12) # Show 25 contacts per page.
      
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        for item in page_obj:
            item.sale_price ="₫{:,.0f}".format(item.sale_price)
        context['page_obj']= page_obj

        return render(request, "homepage/home-page.html",context)