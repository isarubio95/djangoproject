from django.db import models
from django.conf import settings
from django.utils import timezone

# 1. El catálogo: Aquí guardas "Sentadilla", "Press Militar", etc.
class TipoEjercicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='ejercicios/', null=True, blank=True)
    
    class Meta:
        verbose_name = "Tipo de Ejercicio"
        verbose_name_plural = "Tipos de Ejercicios"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# 2. La sesión de entrenamiento
class Actividad(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Nombre de la sesión")
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="actividades"
    )
    fecha = models.DateTimeField(default=timezone.now)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha.strftime('%d/%m/%Y')}"

# 3. El registro concreto en el entrenamiento
class Ejercicio(models.Model):
    actividad = models.ForeignKey(
        Actividad, 
        on_delete=models.CASCADE, 
        related_name="ejercicios"
    )
    # Ahora es una relación al catálogo, no un CharField
    tipo_ejercicio = models.ForeignKey(
        TipoEjercicio, 
        on_delete=models.PROTECT, 
        verbose_name="Ejercicio"
    )
    repeticiones = models.PositiveIntegerField()
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.tipo_ejercicio.nombre} - {self.repeticiones} reps ({self.peso_kg}kg)"