from django.db import models


class Propietario(models.Model):
    documento = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
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


class Cita(models.Model):
    # Relación con la mascota que recibe la cita
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='citas'
    )

    # Fecha de la cita
    fecha = models.DateField()

    # Hora de la cita
    hora = models.TimeField()

    # Motivo principal de la cita médica
    motivo = models.TextField()

    # Observaciones opcionales del veterinario
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            f"Cita para {self.mascota.nombre} el {self.fecha} "
            f"a las {self.hora}"
        )

# Create your models here.
