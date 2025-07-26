from django.db import models


class Propietario(models.Model):
    """Representa al dueño de una mascota."""
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre


class Mascota(models.Model):
    """Representa a una mascota atendida en la clínica."""
    ESPECIE_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50, choices=ESPECIE_CHOICES)
    edad = models.PositiveIntegerField()
    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.CASCADE,
        related_name='mascotas',
    )

    def __str__(self) -> str:
        return f"{self.nombre} ({self.especie})"


# Create your models here.
