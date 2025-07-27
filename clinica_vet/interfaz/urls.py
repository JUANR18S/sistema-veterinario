# urls.py en la app interfaz

from django.urls import path
from . import views

# Namespace de la app
app_name = 'interfaz'

urlpatterns = [
    # Vistas principales
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('placeholder/', views.placeholder, name='placeholder'),

    # CRUD Propietarios
    path('propietarios/', views.propietario_list, name='propietario_list'),
    path(
        'propietarios/crear/',
        views.propietario_create,
        name='propietario_create'
    ),
    path(
        'propietarios/editar/<int:pk>/',
        views.propietario_editar,
        name='propietario_editar'
    ),
    path(
        'propietarios/eliminar/<int:pk>/',
        views.propietario_eliminar,
        name='propietario_eliminar'
    ),


    # CRUD Mascotas (puedes adaptar igual)
    path('mascotas/', views.mascota_list, name='mascota_list'),
    path('mascotas/crear/', views.mascota_create, name='mascota_create'),

    path(
        'mascotas/editar/<int:pk>/',
        views.mascota_editar,
        name='mascota_editar'
    ),
    path(
        'mascotas/eliminar/<int:pk>/',
        views.mascota_eliminar,
        name='mascota_eliminar'
    ),

]
