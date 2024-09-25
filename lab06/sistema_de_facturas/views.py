from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Vista de inicio de sesión
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User  # Asegúrate de importar User
@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar credenciales fijas
        if username == "admin" and password == "123":
            user, created = User.objects.get_or_create(username=username)
            login(request, user)  # Iniciar sesión
            return redirect('admin_panel')  # Redirige al panel de administración
        else:
            print("Credenciales incorrectas")  # Para depurar
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})

    return render(request, 'login.html')
# Vista del panel de administración
@login_required
def admin_panel(request):
    return render(request, 'admin_panel.html')  # Asegúrate de que este archivo exista

# Propietarios
