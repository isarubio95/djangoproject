from django.db import models
from django.conf import settings
from django.utils import timezone

class Actividad(models.Model):
    # Tipos de rutinas predefinidos
    TIPO_RUTINA = [
        ('CARDIO', 'Cardio'),
        ('FUERZA', 'Entrenamiento de Fuerza'),
        ('YOGA', 'Yoga/Flexibilidad'),
        ('NATACION', 'Natación'),
    ]
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="actividades"
    )
    tipo = models.CharField(
        max_length=20,
        choices=TIPO_RUTINA,
        default='CARDIO'
    )
    duracion_minutos = models.PositiveIntegerField(help_text="Tiempo en minutos")
    fecha = models.DateTimeField(default=timezone.now)
    comentarios = models.TextField(blank=True, null=True)
    calorias_quemadas = models.PositiveIntegerField(help_text="Calorías quemadas durante la actividad", null=True)

    def __str__(self):
        return f"{self.tipo} - {self.usuario.username} ({self.fecha.strftime('%d/%m/%Y')})"