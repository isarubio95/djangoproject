from django.contrib import admin
from django.urls import path, include
from exampleapp.views import homeView
import django.contrib.auth.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
]