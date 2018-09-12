from django.shortcuts import render
from .models import *

# Create your views here.
def lists(request):
    return render(request, 'zeroNine/list.html', {})

def main(request):
    return render(request, 'zeroNine/main.html', {})
