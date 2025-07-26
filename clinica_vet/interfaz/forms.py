from django import forms
from .models import Mascota, Propietario


class PropietarioForm(forms.ModelForm):
    """Formulario para crear y actualizar propietarios."""
    class Meta:
        model = Propietario
        fields = ['nombre', 'telefono', 'email']


class MascotaForm(forms.ModelForm):
    """Formulario para crear y actualizar mascotas."""
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'propietario']
