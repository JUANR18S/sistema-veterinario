from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, Propietario, Cita
from .forms import MascotaForm, PropietarioForm, CitaForm


# 🏠 Página de inicio
def inicio(request):
    return render(request, 'inicio.html')


# 🩺 Página de servicios
def servicios(request):
    return render(request, 'servicios.html')


# 🛠️ Página en construcción
def placeholder(request):
    return render(request, 'placeholder.html')


# 👤 Crear propietario nuevo
def propietario_create(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interfaz:propietario_list')  # ✅ con namespace
    else:
        form = PropietarioForm()
    return render(
        request,
        'propietarios/propietario_form.html',
        {'form': form}
    )


# 📋 Ver listado de propietarios
def propietario_list(request):
    propietarios = Propietario.objects.all()
    return render(
        request,
        'propietarios/propietario_list.html',
        {'propietarios': propietarios}
    )


# ✏️ Editar un propietario existente
def propietario_editar(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('interfaz:propietario_list')  # ✅ con namespace
    else:
        form = PropietarioForm(instance=propietario)
    return render(
        request,
        'propietarios/propietario_form.html',
        {'form': form}
    )


# 🗑️ Eliminar un propietario
def propietario_eliminar(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == 'POST':
        propietario.delete()
        return redirect('interfaz:propietario_list')
    return render(
        request,
        'propietarios/propietario_confirm_delete.html',
        {'propietario': propietario}
    )


# 🐶 Crear mascota nueva
def mascota_create(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interfaz:mascota_list')
    else:
        form = MascotaForm()
    return render(request, 'mascotas/mascota_form.html', {'form': form})


# 🐾 Ver lista de mascotas
def mascota_list(request):
    mascotas = Mascota.objects.select_related('propietario').all()
    return render(
        request,
        'mascotas/mascota_list.html',
        {'mascotas': mascotas}
    )


# Editar Mascota✍️
def mascota_editar(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('interfaz:mascota_list')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mascotas/mascota_form.html', {'form': form})


# 🗑️ Eliminar mascota
def mascota_eliminar(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('interfaz:mascota_list')


# 🗓️ Lista de citas
def cita_list(request):
    citas = Cita.objects.select_related(
        'mascota',
        'mascota__propietario'
    ).all()
    return render(
        request,
        'citas/cita_list.html',
        {'citas': citas}
    )


# Crear cita
def cita_create(request):
    form = CitaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('interfaz:cita_list')
    return render(
        request,
        'citas/cita_form.html',
        {
            'form': form,
            'titulo': 'Crear cita'
        }
    )


# Editar/actualizar cita
def cita_update(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    form = CitaForm(request.POST or None, instance=cita)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('interfaz:cita_list')
    return render(
        request,
        'citas/cita_form.html',
        {
            'form': form,
            'titulo': 'Editar cita'
        }
    )


# Eliminar cita (con confirmación simple)
def cita_delete(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('interfaz:cita_list')
    return render(
        request,
        'citas/cita_confirm_delete.html',
        {'cita': cita}
    )
