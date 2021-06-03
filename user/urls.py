
from django.urls import path
from .views import *
app_name='user'
urlpatterns = [
    # path('search/',CategoryView.as_view(),name="search"),
   
    path('purchase/',OrderPurchase.as_view(),name="purchase"),
    path('address/add',Add_Address.as_view(),name="add"),
    path('address/edit/',Edit_Address.as_view(),name="edit"),
    path('address/delete/',Delete_Address.as_view(),name="delete"),
    path('address/',AddressView.as_view(),name="address"),
    path('comment/',CommentProduct.as_view(),name="comment"),

]
