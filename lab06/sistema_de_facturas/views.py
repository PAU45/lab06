# sistema_de_facturas/views.py
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        # Lógica para manejar el inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Aquí iría la validación del usuario

        # Si la validación es exitosa
        return render(request, 'admin_panel.html')  # Redirigir a un dashboard u otra página

    return render(request, 'login.html')  # Renderizar el formulario de inicio de sesión