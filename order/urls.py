from django.urls import path
from .views import *
app_name='order'
urlpatterns = [
 
    # path('',CartView.as_view(),name="index"),
    path('addOrder/',AddOrder.as_view(),name="addOrder"),
    path('getOrder/',GetRatingOrder.as_view(),name="getOrder"),
    path('manage/',OrderManage.as_view(),name="manage"),
    path('status/',OrderStatus.as_view(),name="status"),
]
