from django import forms
from .models import Mascota, Propietario, Cita


class PropietarioForm(forms.ModelForm):
    """Formulario para crear y actualizar propietarios."""
    class Meta:
        model = Propietario
        fields = ['documento', 'nombre', 'telefono', 'email']


class MascotaForm(forms.ModelForm):
    """Formulario para crear y actualizar mascotas."""
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'propietario']


# ✅ NUEVO: formulario para Cita con inputs nativos de fecha y hora
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['mascota', 'fecha', 'hora', 'motivo', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'motivo': forms.Textarea(attrs={'rows': 3}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
 