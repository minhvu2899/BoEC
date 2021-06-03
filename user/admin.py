from django.contrib import admin
from user.models import Address, Comment, CustomerUser
# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(Address)
admin.site.register(Comment)