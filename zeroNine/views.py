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
    products = Product.objects.all()
    return render(request, 'zeroNine/main.html', {'products':products})

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