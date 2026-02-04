from django.contrib import admin
from .models import Actividad

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'duracion_minutos', 'fecha', 'calorias_quemadas')
    list_filter = ('tipo', 'usuario')