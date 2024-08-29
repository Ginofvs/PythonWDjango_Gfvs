# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta básica que apunta a una vista llamada 'home'
]
