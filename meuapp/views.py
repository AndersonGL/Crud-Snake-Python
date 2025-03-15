from django.shortcuts import render
from meuapp.forms import CarroForm


def home(request):
    return render(request, 'index.html')
   


def form(request):
    data = {}
    data['form'] = CarroForm()          # mandando o form para o form.html
    return render(request, 'form.html', data )
