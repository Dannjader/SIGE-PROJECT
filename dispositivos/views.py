from django.shortcuts import render
from dispositivos.models import Reporte, Dispositivo, Servicio

# # Create your views here.
def inicio(request):
    return render(request, 'index.html')


def dispositivos_list(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'dispositivos_list.html', {'dispositivos': dispositivos})


def servicios_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios_list.html', {'servicios': servicios})


def reporte_list(request):
    reportes = Reporte.objects.all()
    return render(request, 'reporte_list.html', {'reportes': reportes})
