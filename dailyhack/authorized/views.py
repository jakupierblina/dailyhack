from django.shortcuts import render

from dailyhack.base import views
# Create your views here.
def index(request):
    context = {}
    return render(request, 'authorized/index.html', context)
