from django.shortcuts import render

from dailyhack.base import views
# Create your views here.
def index(request):
    context = {}
    return render(request, 'authorized/index.html', context)



def diary(request):
    context = {}
    return render(request, 'authorized/diary.html', context)



def todo(request):
    context = {}
    return render(request, 'authorized/todo.html', context)


def calendar(request):
    context = {}
    return render(request, 'authorized/calendar.html', context)