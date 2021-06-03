from django.contrib import admin
from product.models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields=('title',)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
