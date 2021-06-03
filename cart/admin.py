from cart.models import CartItem
from django.contrib import admin
from cart.models import *
# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
