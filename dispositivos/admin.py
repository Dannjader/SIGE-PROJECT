from django.contrib import admin
from .models import Reporte, Responsable, Dispositivo, Servicio, Tecnico

# Register your models here.


class ReporteAdmin(admin.ModelAdmin):
    list_display = ('id','responsable','tecnico')
    list_filter = ('dispositivos', 'servicio', 'tecnico', 'responsable')
    list_display_links = ()

class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('tipo_dispositivo','serial', 'marca','modelo')
    list_filter = ('id','activo_nuevo','responsable')
    list_display_links = ('tipo_dispositivo',)


class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','cargo')
    list_filter = ('nombre', 'apellido', 'cargo')


admin.site.register(Reporte, ReporteAdmin) 
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(Servicio)
admin.site.register(Tecnico)
