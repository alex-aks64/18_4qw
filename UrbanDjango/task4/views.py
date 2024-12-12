
from django.shortcuts import render

def index(request):
    return render(request, 'fourth_task/index.html')

def index3(request):
    return render(request, 'fourth_task/index3.html')

def index2(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077','PayDay']}
    return render(request, 'fourth_task/index2.html', context)
# Create your views here.
