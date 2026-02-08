from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import ActividadForm, DaisySignupForm, EjercicioFormSet
from .models import Actividad, Serie
from django.http import JsonResponse

class SignUpView(generic.CreateView):
    form_class = DaisySignupForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required
def editar_actividad(request, actividad_id):
    actividad = get_object_or_404(Actividad, id=actividad_id, usuario=request.user)
    is_modal = request.GET.get('modal') == 'true'

    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            if is_modal:
                # Si es modal, devolvemos JSON para que JS cierre el modal sin recargar
                return JsonResponse({'success': True})
            return redirect('home')
    else:
        form = ActividadForm(instance=actividad)
    
    return render(request, 'editar_actividad.html', {
        'form': form,
        'actividad': actividad,
        'is_modal': is_modal,
        'base_template': 'base_modal.html' if is_modal else 'base.html'
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
        formset = EjercicioFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            actividad = form.save(commit=False)
            actividad.usuario = request.user  # Vinculamos la actividad al usuario actual
            actividad.save()
            
            # Guardamos los ejercicios y procesamos las series manualmente
            for form_ej in formset:
                if form_ej.is_valid() and form_ej.cleaned_data and not form_ej.cleaned_data.get('DELETE'):
                    ejercicio = form_ej.save(commit=False)
                    ejercicio.actividad = actividad
                    ejercicio.save()

                    # Procesar series desde request.POST usando el prefijo del form
                    prefix = form_ej.prefix
                    i = 0
                    while True:
                        reps_key = f'{prefix}-series-{i}-repeticiones'
                        peso_key = f'{prefix}-series-{i}-peso_kg'
                        if reps_key in request.POST and peso_key in request.POST:
                            Serie.objects.create(
                                ejercicio=ejercicio,
                                numero_serie=i+1,
                                repeticiones=request.POST[reps_key],
                                peso_kg=request.POST[peso_key]
                            )
                            i += 1
                        else:
                            break
            
            return redirect('home')
    else:
        form = ActividadForm()
        formset = EjercicioFormSet()
    return render(request, "index.html", {'form': form, 'formset': formset})

@login_required
def rutinas_json(request):
    actividades = Actividad.objects.filter(usuario=request.user)
    eventos = []
    for act in actividades:
        eventos.append({
            'id': act.id,
            'title': act.titulo,
            'start': act.fecha.isoformat(),
            # Calculamos el fin sumando la duración si quieres que ocupe espacio
            'backgroundColor': '#570df8',
            'borderColor': '#570df8',
        })
    return JsonResponse(eventos, safe=False)