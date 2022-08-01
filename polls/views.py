from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hola</h1>')

def data(request):
    name = 'jose'
    cores = ["uno","dos","tres"]

    return render(request=request, template_name="index.html", context={'name': name, 'cores': cores})
