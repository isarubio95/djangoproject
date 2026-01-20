from django.contrib import admin
from django.urls import path, include
from exampleapp.views import homeView, SignUpView, eliminar_actividad, editar_actividad
import django.contrib.auth.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path('eliminar/<int:actividad_id>/', eliminar_actividad, name='eliminar_actividad'),
    path('editar/<int:actividad_id>/', editar_actividad, name='editar_actividad'),
]