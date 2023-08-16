from django.urls import path
from .views import inicio, dispositivos_list, reporte_list, servicios_list

urlpatterns = [
    path('', inicio, name='inicio'),
    path('dispositivos/', dispositivos_list, name='dispositivos'),
    path('servicios/', servicios_list, name='servicios'),
    path('reportes/', reporte_list, name='reportes'),
]
