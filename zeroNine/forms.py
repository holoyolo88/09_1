from django import forms

from .models import User,Product

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('userName', 'password','student_num')

class ProductForm(forms.ModelForm):

    class Mea:
        model= Product
        fileds = ('userid','category','productName','facebook_addr','url','member_num','site_name', 'price', 'productType')