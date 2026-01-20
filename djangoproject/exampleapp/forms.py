from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Actividad

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['tipo', 'duracion_minutos', 'comentarios', 'fecha']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'duracion_minutos': forms.NumberInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Ej: 45'}),
            'comentarios': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full', 'rows': 2}),
            'fecha': forms.DateTimeInput(attrs={'class': 'input input-bordered w-full', 'type': 'datetime-local'}),
        }

class DaisySignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input input-bordered w-full'})

class DaisyLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input input-bordered w-full'})