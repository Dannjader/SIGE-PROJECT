from django.contrib import admin
from dispositivos.models import Dispositivo, Responsable, Servicio


class DispositivoAdmin(admin.ModelAdmin):
    list_display = ['tipo_dispositivo', 'activo_nuevo']

class ResponsableAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email']
    
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre_servicio','descripcion', 'dispositivo']
    
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(Servicio, ServicioAdmin)
