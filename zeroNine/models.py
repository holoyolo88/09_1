from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    password = models.CharField(max_length=64,default="")
    student_num = models.CharField(max_length=16,default="")
    userName = models.CharField(max_length=32,default="")

#class Category(models.Model):
    #category = models.CharField(max_length=64, primary_key=True)

# null허용 여부와 blank 허용 옵션의 디폴트 값은 False
class Product(models.Model):
    userid = models.ForeignKey('User', on_delete = models.CASCADE)
    category=models.CharField(max_length = 64,default="")
    productName = models.CharField(max_length=64,default="")
    #start_time = models.DateTimeField()
    #end_time = models.DateTimeField()
    facebook_addr = models.CharField(max_length=128,default="")
    url = models.CharField(max_length=128,default="")
    member_num = models.IntegerField(default=0)
    #notice = models.TextField()
    site_name = models.CharField(max_length=128,default="")
    img_path = models.CharField(max_length=128,default="")
    price = models.IntegerField(default=0)
    direct = models.IntegerField(default=0)

    
#class Product_has_User(models.Model):
    #order_date = models.IntegerField(max_length=128)
    #order_option = models.CharField(max_length=64)
    #product_url = models.CharField(max_length=64)
    #Product_idx = models.ForeignKey('Product', on_delete = models.CASCADE)
    #User_id = models.ForeignKey('User', on_delete = models.CASCADE)

#class Order(models.Model):
    #Product_idx = models.OneToOneField('Product', on_delete = models.CASCADE)
    #order_id = models.CharField(max_length=64)
