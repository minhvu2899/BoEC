from django.contrib import admin
from product.models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields=('title',)
    list_filter=('active',)
    list_display=('title','price',)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductOption)
admin.site.register(ProductOptionValue)
