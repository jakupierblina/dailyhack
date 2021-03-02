"""dailyhack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#import base first
from dailyhack.base import views as baseviews
from dailyhack.authorized import views as authorizedviews




#import authorized -- authorized is when a person has an account in the website

urlpatterns = [
    path('admin/', admin.site.urls),

    #call base
    path('', baseviews.base, name='base'),
    path('login/', baseviews.loginPage, name='login'),
    path('register/', baseviews.registerPage, name='register'),
    path('logout/', baseviews.logoutUser, name='logout'),

    path('welcome/', authorizedviews.index, name='welcome'),

]
