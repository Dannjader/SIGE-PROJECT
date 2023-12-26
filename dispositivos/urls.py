from django.urls import path
from dispositivos.views import inicio, dispositivos_list, servicios_list, login_view

urlpatterns = [
    path('', login_view, name='login'),
<<<<<<< HEAD
    path('', inicio, name='inicio'),
    path('dispositivos/', dispositivos_list, name='dispositivos'),
    path('servicios/', servicios_list, name='servicios'),
=======
    path('inicio/', inicio, name='inicio'),
    path('dispositivos/', dispositivos_list, name='dispositivos'),
    path('servicios/', servicios_list, name='servicios'),
    path('reportes/', reporte_list, name='reportes'),
    
>>>>>>> stayling
]
