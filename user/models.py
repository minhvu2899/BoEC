from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Product
from django.db.models.deletion import CASCADE
# Create your models here.



    
class CustomerUser(AbstractUser):
    phone_number =models.CharField(default='',max_length=15)
class Address(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    street =models.CharField(default='',max_length=255)
    apartment_number =models.CharField(default='',max_length=255)
    district=models.CharField(default='',max_length=255)
    city=models.CharField(default='',max_length=255)
    default=models.BooleanField(default=False)
    def ToString(self):
        return self.street+"," +self.apartment_number+","+self.district+","+ self.city

class Comment(models.Model):
    user = models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(default='')
    rating = models.IntegerField(default=0)
    order_id = models.IntegerField(default=0)
    create_at =models.DateTimeField(auto_now_add=True)

