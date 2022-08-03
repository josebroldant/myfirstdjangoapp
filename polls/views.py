from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Conversor, CategoryForm

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hola</h1>')

def data(request):
    name = 'jose'
    cores = ["uno","dos","tres"]

    return render(request=request, template_name="index.html", context={'name': name, 'cores': cores})

def conversor(request):
    # Preciso criar uma instancia do formulario
    # Como acessar as informacoes do formulario enviadas na request.
    if request.method == 'POST':
        form = Conversor(request.POST)
        if form.is_valid():
            print("OS DADOS SAO VALIDOS!!!")
    else:
        form = Conversor()
    print("ENTROU AQUI NA VIEW!!!")
    return render(
        request=request,
        template_name='polls/conversor.html',
        context={
            'form': form,
        }
    )