from django.contrib import admin
from .models import Responsable, Dispositivo, Servicio, Tecnico, Reporte

# Register your models here.
admin.site.register(Responsable)
admin.site.register(Dispositivo)
admin.site.register(Servicio)
admin.site.register(Tecnico)
admin.site.register(Reporte)