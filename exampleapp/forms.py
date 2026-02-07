from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Actividad, Ejercicio

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['titulo', 'comentarios', 'fecha']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input input-bordered w-full', 'placeholder': 'Ej: Empuje - Pecho/Hombro'}),
            'comentarios': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full', 'rows': 2}),
            'fecha': forms.DateTimeInput(attrs={'class': 'input input-bordered w-full', 'type': 'datetime-local'}),
        }

class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = ['tipo_ejercicio', 'repeticiones', 'peso_kg']
        widgets = {
            'tipo_ejercicio': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'repeticiones': forms.NumberInput(attrs={'class': 'input input-bordered w-full'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'input input-bordered w-full'}),
        }

EjercicioFormSet = inlineformset_factory(
    Actividad,
    Ejercicio,
    form=EjercicioForm,
    extra=1,  # Número de ejercicios vacíos que aparecen por defecto
    can_delete=True
)

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