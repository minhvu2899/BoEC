from django.db import models
from cart.models import Cart
from user.models import CustomerUser
from product.models import Product
# Create your models here.
STATUS = [
    (1, 'Chờ xác nhận'),
    (2, 'Đang xử lí'),
    (3, 'Đang giao hàng'),
    (4, 'Đã hoàn thành'),
    (5, 'Đã hủy'),
]    
class Shipping(models.Model):
    title = models.CharField(max_length=255)
    shipping_fee = models.FloatField(default=0)
    def __str__(self):
        return self.title
class Payment(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
class Order(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    shipping_address =models.CharField(default='',max_length=255)
    total = models.FloatField(default=0)
    ship = models.ForeignKey(Shipping,on_delete=models.CASCADE,null=True,blank=True)
    paymentMethod = models.ForeignKey(Payment,on_delete=models.CASCADE,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
      
        choices=STATUS,
        default=STATUS[0],
    )
    is_complete =models.BooleanField(default=False)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_name= models.CharField(max_length=255,null=True)
    image= models.CharField(max_length=255,null=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
   
    is_rating = models.BooleanField(default=False)
    def formatPrice(self):
        self.price ="₫{:,.0f}".format(self.price)
        return self.price