from django.contrib import admin
from django.urls import path, include
from exampleapp.views import homeView, SignUpView, eliminar_actividad, editar_actividad, rutinas_json
import django.contrib.auth.urls
from django.contrib.auth import views as auth_views
from exampleapp.forms import DaisyLoginForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=DaisyLoginForm), 
        name='login'),
    path('eliminar/<int:actividad_id>/', eliminar_actividad, name='eliminar_actividad'),
    path('editar/<int:actividad_id>/', editar_actividad, name='editar_actividad'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('api/rutinas/', rutinas_json, name='rutinas_json'),
]