from django.shortcuts import render, get_object_or_404, redirect
from .forms import MarcaForm
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

def eliminar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)  # Obtiene la marca por el id (pk)
    if request.method == 'POST':
        marca.delete()  # Elimina la marca
        return redirect('lista-marcas')  # Redirige a la lista de marcas
    return render(request, 'products/confirmar_eliminacion.html', {'marca': marca})

def actualizar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)  # Obtiene la marca por id
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)  # Pasa el formulario con los datos actuales
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('lista-marcas')  # Redirige a la lista de marcas
    else:
        form = MarcaForm(instance=marca)  # Si es un GET, muestra el formulario con los datos actuales
    return render(request, 'products/actualizar_marca.html', {'form': form}) 