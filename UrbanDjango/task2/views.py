from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'second_task/index.html')

def index2(request):
    return render(request, 'second_task/index2.html')

def index3(request):
    return render(request, 'second_task/index3.html')