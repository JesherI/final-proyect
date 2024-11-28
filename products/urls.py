from django.urls import path
from . import views

urlpatterns = [
    path('marcas/', views.lista_marcas, name='lista-marcas'),
    path('crear-marcas/', views.crear_marca, name='crear-marca'),
]
