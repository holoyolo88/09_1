from django.shortcuts import render
from .models import *

# Create your views here.
def lists(request):
    return render(request, 'zeroNine/list.html', {})

def apply_db(request):
    return render(request, 'zeroNine/apply_db.html', {})

def apply(request):
    return render(request, 'zeroNine/apply.html', {})

def cancel(request):
    return render(request, 'zeroNine/cancel.html', {})

def login(request):
    return render(request, 'zeroNine/login.html', {})

def main(request):
    name1 = Product.objects.get(pk=1)
    price1 = Product.objects.get(pk=1)
     name2 = Product.objects.get(pk=1)
    price2 = Product.objects.get(pk=1)
     name3 = Product.objects.get(pk=1)
    price3 = Product.objects.get(pk=1)
     name4 = Product.objects.get(pk=1)
    price4 = Product.objects.get(pk=1)
     name5 = Product.objects.get(pk=1)
    price5 = Product.objects.get(pk=1)
     name6 = Product.objects.get(pk=1)
    price6 = Product.objects.get(pk=1)
     name7 = Product.objects.get(pk=1)
    price7 = Product.objects.get(pk=1)
     name8 = Product.objects.get(pk=1)
    price8 = Product.objects.get(pk=1)
    return render(request, 'zeroNine/main.html', { 'lists' : [ {'name1':name1, 'price1':price1},{'name2':name2, 'price2':price2},{'name3':name3, 'price3':price3},{'name4':name4, 'price4': price4}{'name5':name5,'price5':price5}{'name6':name6,'price6':price6}{'name7':name7, 'price7':price7}{'name8':name8, 'price8':price8}]})

def order(request):
    return render(request, 'zeroNine/order.html', {})

def participant(request):
    return render(request, 'zeroNine/participant.html', {})

def productpage_db(request):
    return render(request, 'zeroNine/productpage_db.html', {})

def productpage(request):
    return render(request, 'zeroNine/productpage.html', {})

def registration(request):
    return render(request, 'zeroNine/registration.html', {})