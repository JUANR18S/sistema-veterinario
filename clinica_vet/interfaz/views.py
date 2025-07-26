from django.shortcuts import render, redirect
from .models import Mascota, Propietario
from .forms import MascotaForm, PropietarioForm


def inicio(request):
    """Página de inicio."""
    return render(request, 'inicio.html')


def servicios(request):
    """Página de servicios."""
    return render(request, 'servicios.html')


def placeholder(request):
    """Página temporal en construcción."""
    return render(request, 'placeholder.html')


def propietario_create(request):
    """Registra un nuevo propietario mediante un formulario."""
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propietario_list')
    else:
        form = PropietarioForm()
    return render(
        request,
        'propietarios/propietario_form.html',
        {'form': form}
    )


def propietario_list(request):
    """Muestra la lista de propietarios existentes."""
    propietarios = Propietario.objects.all()
    return render(
        request,
        'propietarios/propietario_list.html',
        {'propietarios': propietarios}
    )


def mascota_create(request):
    """Registra una nueva mascota."""
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota_list')
    else:
        form = MascotaForm()
    return render(request, 'mascotas/mascota_form.html', {'form': form})


def mascota_list(request):
    """Lista las mascotas registradas."""
    mascotas = Mascota.objects.select_related('propietario').all()
    return render(
        request,
        'mascotas/mascota_list.html',
        {'mascotas': mascotas}
    )
