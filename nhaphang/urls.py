from django import views
from django.urls import path
from . import views 
app_name='nhaphang'
urlpatterns = [
    path('index/',views.index,name='kho'),
    path('xemsp',views.xemsanpham,name='xemsp'),
    path('nhap',views.nhaphang,name='nhap')
]