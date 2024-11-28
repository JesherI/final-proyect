from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre  

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)