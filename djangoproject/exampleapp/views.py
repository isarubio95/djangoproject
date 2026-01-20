from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ActividadForm, DaisySignupForm
from .models import Actividad

class SignUpView(generic.CreateView):
    form_class = DaisySignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def editar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id, usuario=request.user)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'editar_actividad.html', {
        'form': form,
        'actividad': actividad
    })

@login_required
def eliminar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id, usuario=request.user)
    if request.method == 'POST':
        actividad.delete()
        return redirect('home')
    return render(request, "confirmar_borrado.html", {'actividad': actividad})

@login_required
def homeView(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.usuario = request.user  # Vinculamos la actividad al usuario actual
            actividad.save()
            return redirect('home')
    else:
        form = ActividadForm()
    return render(request, "index.html", {'form': form})