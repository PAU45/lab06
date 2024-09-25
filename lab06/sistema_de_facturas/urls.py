from django.urls import path
from . import views

# sistema_de_facturas/urls.py
from django.urls import path
from .views import login_view  # Importa la vista directamente

urlpatterns = [
    path('login/', login_view, name='login'),  # Ruta para el inicio de sesión
]