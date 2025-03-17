from django.shortcuts import render, redirect
from django.http import HttpResponse
from meuapp.forms import CarroForm
from meuapp.models import Carro



def home(request):
    data = {}
    data['db'] = Carro.objects.all()
    return render(request, 'index.html', data)
   


def form(request):
    data = {}
    data['form'] = CarroForm()          # mandando o form para o form.html
    return render(request, 'form.html', data )




def create(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():  # valida 
        form.save()      # salva no banco de dados
        return redirect ('home')  # retorna para home
    
    
def view (request, pk):
    data = {}
    data['db'] = Carro.objects.get(pk=pk)
    return render(request, 'view.html', data)
    