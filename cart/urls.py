from django.urls import path
from .views import *
app_name='cart'
urlpatterns = [
 
    path('',CartView.as_view(),name="index"),
    path('checkout/',CheckoutView.as_view(),name="checkout"),
    path('update/',UpdateCart.as_view(),name="update"),

    path('addCart/',AddCart.as_view(),name="addToCart"),
]
