from django.db import models


class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Dispositivo(models.Model):
    tipo_dispositivo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    activo_viejo = models.CharField(max_length=100)
    activo_nuevo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo_dispositivo} {self.activo_nuevo}'


class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nombre_servicio} {self.descripcion}{self.dispositivo}'
