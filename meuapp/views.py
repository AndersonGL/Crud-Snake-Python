from django.shortcuts import render, redirect
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


def edit (request, pk):
    data = {}
    data['db'] = Carro.objects.get(pk=pk)
    data['form'] = CarroForm(instance=data['db'])
    return render(request, 'form.html', data)
    

def update(request, pk):
    data = {}
    data['db']= Carro.objects.get(pk=pk)
    form = CarroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')
    
def delete(request, pk):
    db = Carro.objects.get(pk=pk)
    db.delete()
    return redirect('home')
