from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from dispositivos.models import Dispositivo, Responsable, Servicio, CustomUser


class DispositivoAdmin(admin.ModelAdmin):
    list_display = ['tipo_dispositivo', 'activo_nuevo']

class ResponsableAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','cargo','email']
    
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre_servicio','descripcion', 'dispositivo']

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(CustomUser, UserAdmin)    

