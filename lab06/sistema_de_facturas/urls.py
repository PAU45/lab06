from django.urls import path
from .views import login_view
from .views import admin_panel_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('admin-panel/', admin_panel_view, name='admin_panel'),  # Asegúrate de definir esta vista
]