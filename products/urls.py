from django.urls import path
from . import views

urlpatterns = [
    path('marcas/', views.lista_marcas, name='lista-marcas'),
    path('crear-marcas/', views.crear_marca, name='crear-marca'),
    path('eliminar-marca/<int:pk>/', views.eliminar_marca, name='eliminar-marca'),  # URL para eliminar
    path('actualizar-marca/<int:pk>/', views.actualizar_marca, name='actualizar-marca'),  # URL para actualizar
]