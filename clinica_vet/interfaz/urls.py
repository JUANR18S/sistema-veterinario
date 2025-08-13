# interfaz/urls.py

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

    # CRUD Mascotas
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

    # ✅ Citas
    path('citas/', views.cita_list, name='cita_list'),
    path('citas/crear/', views.cita_create, name='cita_create'),
    path('citas/<int:pk>/editar/', views.cita_update, name='cita_update'),
    path('citas/<int:pk>/eliminar/', views.cita_delete, name='cita_delete'),
]
