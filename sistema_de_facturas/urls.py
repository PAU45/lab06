from django.urls import path
from .views import login_view
from .views import admin_panel_view
from .views import crear_factura
from .views import factura_detalle
from .views import  factura_pdf
urlpatterns = [
    path('', login_view, name='login'),
    path('admin-panel/', admin_panel_view, name='admin_panel'),  # Asegúrate de definir esta vista
    # urls.py



path('crear-factura/', crear_factura, name='crear_factura'),
path('factura/<str:numero>/',factura_detalle, name='factura_detalle'),  # Ruta para factura_detalle


     path('factura/<str:numero>/pdf/', factura_pdf, name='factura_pdf'),
]



