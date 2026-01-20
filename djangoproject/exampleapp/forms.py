from django import forms
from .models import Actividad

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['tipo', 'duracion_minutos', 'comentarios', 'fecha']
        widgets = {
            'comentarios': forms.Textarea(attrs={'rows': 2, 'placeholder': '¿Qué tal te ha ido?'}),
        }