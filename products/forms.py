from django import forms
from .models import Marca, Producto

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'description']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'marca'] 
