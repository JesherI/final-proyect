from django.shortcuts import render, redirect
from .models import Marca
# Create your views here.

def crear_marca(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        description = request.POST.get('description')
        if nombre and description:
            Marca.objects.create(nombre=nombre, description=description)
            return redirect('lista-marcas')
    return render(request, 'products/createmarca.html')

def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'products/listamarca.html', {'marcas': marcas})