from django.shortcuts import render, redirect
from .models import *
from .forms import UserForm

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

def join(request):
    #form = UserForm() 'form':form
    return render(request, 'zeroNine/join.html',{})

def join_db(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # login 으로 redirect
            # js 처리 결과 alert
            return redirect('main')
        return redirect('main')

def signup(request):
    User.objects.create(
        userName = request.POST['id'],
        password = request.POST['password'],
        student_num = request.POST['student-number'])

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