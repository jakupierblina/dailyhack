from django.shortcuts import render

# Create your views here.

def base(request):
    context = {}
    return render(request, 'base/base.html', context)

def login(request):
    context = {}
    return render(request, 'base/login.html', context)

def register(request):
    context = {}
    return render(request, 'base/register.html', context)
