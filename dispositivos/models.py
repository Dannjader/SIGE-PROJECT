from datetime import datetime
from django.db import models

# Create your models here.


class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self['nombre', 'apellido', 'cargo']


class Dispositivo(models.Model):
    serial = models.CharField(max_length=50)
    tipo_dispositivo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    activo_viejo = models.CharField(max_length=25)
    activo_nuevo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)


def __str__(self):
    return self['serial', 'tipo', 'marca', 'modelo', 'activo_viejo', 'activo_nuevo', 'ubicacion']


class Servicio(models.Model):
    CHOICES = (
        ('error', 'Error'),
        ('mejora', 'Mejora'),
        ('nueva funcionalidad', 'Nueva Funcionalidad'),
    )
    tipo_servicio = models.CharField(max_length=100, choices=CHOICES)
    requerimiento = models.CharField(max_length=200)
    solucion = models.TextField(max_length=1000)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    dispositivos = models.ManyToManyField(Dispositivo)


def __str__(self):
    return self['tipo_servicio', 'requerimiento', 'solucion', 'fecha_inicio', 'fecha_fin']


class Tecnico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    servicios = models.ManyToManyField(Servicio)


def __str__(self):
    return self['nombre', 'apellido', 'correo']


class Reporte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    dispositivos = models.ManyToManyField(Dispositivo)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)


def __str__(self):
    return self['nombre', 'descripcion', 'dispositivo', 'servicio', 'responsable', 'tecnico'], f"Reporte #{self.id}"
