from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
from product.models import *
class HomeView(View):
    def get(seft,request):
        context={}
        context['list'] =Product.objects.all()
        context['categorys'] = Category.objects.all()
        return render(request, "homepage/home-page.html",context)