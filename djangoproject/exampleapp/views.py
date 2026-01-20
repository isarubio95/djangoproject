from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ActividadForm

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

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