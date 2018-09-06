from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=64)
    student_num = models.CharField(max_length=16)
    name = models.CharField(max_length=32)

class Category(models.Model):
    name = models.CharField(max_length=64, primary_key=True)

# null허용 여부와 blank 허용 옵션의 디폴트 값은 False
class Product(models.Model):
    idx = models.AutoField(primary_key=True)
    #catagory = models.CharField(max_length=64)
    catagory=models.ForeignKey('Category',on_delete = models.CASCADE)
    name = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    facebook_addr = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    member_num = models.IntegerField()
    notice = models.TextField(blank=True)
    site_name = models.CharField(max_length=128)
    img_path = models.CharField(max_length=128)
    price = models.IntegerField()
    direct = models.IntegerField()

    
    
class Product_has_User(models.Model):
    order_date = models.IntegerField()
    order_option = models.CharField(max_length=64)
    product_url = models.CharField(max_length=64)
    Product_idx = models.ForeignKey('Product', on_delete = models.CASCADE)
    User_id = models.ForeignKey('User', on_delete = models.CASCADE)
    order_date = models.IntegerField()
    order_option = models.CharField(max_length=64)
    product_url = models.CharField(max_length=64)

class Order(models.Model):
    Product_idx = models.OneToOneField('Product', on_delete = models.CASCADE)
    Product_idx = models.IntegerField(primary_key=True)
    order_id = models.CharField(max_length=64)
