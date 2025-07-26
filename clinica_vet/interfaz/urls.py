from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('placeholder/', views.placeholder, name='placeholder'),

    # Rutas para propietarios
    path(
        'propietarios/crear/',
        views.propietario_create,
        name='propietario_create'
    ),
    path('propietarios/', views.propietario_list, name='propietario_list'),

    # Rutas para mascotas
    path('mascotas/crear/', views.mascota_create, name='mascota_create'),
    path('mascotas/', views.mascota_list, name='mascota_list'),
]
