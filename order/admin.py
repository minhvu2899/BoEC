from django.contrib import admin

# Register your models here.
from order.models import *
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Shipping)
admin.site.register(Payment)
