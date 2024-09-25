# sistema_de_facturas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        # Lógica para manejar el inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticación del usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Iniciar sesión
            return redirect('admin_panel')  # Redirigir al panel de administración
        else:
            # Si la validación falla, puedes agregar un mensaje de error
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'sistema_de_facturas/login.html', {'error': error_message})

    return render(request, 'sistema_de_facturas/login.html')  # Renderizar el formulario de inicio de sesión

def admin_panel_view(request):
    # Verificar si el usuario está autenticado
    if not request.user.is_authenticated:
        return redirect('login')  # Redirigir al login si no está autenticado
    return render(request, 'sistema_de_facturas/admin_panel.html')  # Renderizar el panel de administración