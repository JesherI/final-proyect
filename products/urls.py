from django.urls import path
from . import views

urlpatterns = [
    path('marcas/', views.lista_marcas, name='lista-marcas'),
    path('crear-marcas/', views.crear_marca, name='crear-marca'),
    path('eliminar-marca/<int:pk>/', views.eliminar_marca, name='eliminar-marca'),  
    path('actualizar-marca/<int:pk>/', views.actualizar_marca, name='actualizar-marca'),
    path('productos', views.lista_productos, name='lista-productos'),  
    path('crear-producto/', views.crear_producto, name='crear-producto'),
    path('eliminar-producto/<int:pk>/', views.eliminar_producto, name='eliminar-producto'),
    path('actualizar-producto/<int:pk>/', views.actualizar_producto, name='actualizar-producto'),
]