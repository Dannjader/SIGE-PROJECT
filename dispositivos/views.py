from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from dispositivos.models import Reporte, Dispositivo, Servicio

# # Create your views here.


def inicio(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dispositivos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def dispositivos_list(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'dispositivos_list.html', {'dispositivos': dispositivos})


def servicios_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios_list.html', {'servicios': servicios})


def reporte_list(request):
    reportes = Reporte.objects.all()
    return render(request, 'reporte_list.html', {'reportes': reportes})
