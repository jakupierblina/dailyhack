from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def base(request):
    context = {}
    return render(request, 'base/base.html', context)

def loginPage(request):

    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'base/login.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Profile name' + user +'was created succesfully!')
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'base/register.html', context)


def logoutUser(request):
    logout(request)
    return  redirect('login')