from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(default='',max_length=100)
    slug=models.CharField(max_length=100,default='')
    desc=models.TextField(default='')
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True)
    active=models.BooleanField(default=True)
    list_display = ('title', 'parent_id')
    def __str__(self):
        return "%s %s" %(self.id, self.title)

class Product(models.Model):
    title =models.CharField(default='',max_length=255)
    desc=models.TextField(default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    sale_price=models.IntegerField(default=0,null=True,blank=True)
    inventory=models.IntegerField(default=0,null=True,blank=True)
    thumbnail = models.CharField(default='',max_length=255,null=True)
    active= models.BooleanField(default=True)
    def __str__(self):
        return "%s %s" %(self.title,self.category)
    def formatPrice(self):
        return "₫{:,.0f}".format(self.sale_price)
