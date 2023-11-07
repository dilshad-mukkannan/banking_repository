from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def demo(request):
    return render(request, 'index.html')

def new_page(request):
    return render(request, 'new_page.html')

