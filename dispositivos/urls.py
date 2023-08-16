from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import inicio, dispositivos_list, reporte_list, servicios_list, login_view

urlpatterns = [
    path('', inicio, name='inicio'),
    path('dispositivos/', dispositivos_list, name='dispositivos'),
    path('servicios/', servicios_list, name='servicios'),
    path('reportes/', reporte_list, name='reportes'),
    path('login/', login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
