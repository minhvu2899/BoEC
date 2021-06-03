
from django.urls import path
from .views import *
app_name='product'
urlpatterns = [
 
    path('',ProductView.as_view(),name="index"),
    path('category/<slug:slug>/',CategoryView.as_view(),name="category"),
    path('detail/<int:id>/',DetailView.as_view(),name="detail"),
    path('search/',SearchProduct.as_view(),name="search"),
    # path('create/',CreateProduct.as_view(),name="create"),
]
