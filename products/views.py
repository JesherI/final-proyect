from django.shortcuts import render, get_object_or_404, redirect
from .forms import MarcaForm, ProductoForm
from .models import Marca, Producto
# Create your views here.

def crear_marca(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        description = request.POST.get('description')
        if nombre and description:
            Marca.objects.create(nombre=nombre, description=description)
            return redirect('lista-marcas')
    return render(request, 'marca/createmarca.html')

def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'marca/listamarca.html', {'marcas': marcas})

def eliminar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)  # Obtiene la marca por el id (pk)
    if request.method == 'POST':
        marca.delete()  # Elimina la marca
        return redirect('lista-marcas')  # Redirige a la lista de marcas
    return render(request, 'marca/confirmar_eliminacion.html', {'marca': marca})

def actualizar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)  # Obtiene la marca por id
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)  # Pasa el formulario con los datos actuales
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('lista-marcas')  # Redirige a la lista de marcas
    else:
        form = MarcaForm(instance=marca)  # Si es un GET, muestra el formulario con los datos actuales
    return render(request, 'marca/actualizar_marca.html', {'form': form}) 

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista-productos')  
    else:
        form = ProductoForm()

    return render(request, 'producto/createproducto.html', {'form': form})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/listaproducto.html', {'productos': productos})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)  
    if request.method == 'POST':
        producto.delete()  
        return redirect('lista-productos')  
    return render(request, 'producto/confirmar_eliminacion.html', {'producto': Producto})

def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk) 
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)  
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('lista-productos')  
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto/actualizar_producto.html', {'form': form}) 
