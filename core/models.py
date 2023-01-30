from django.db import models

# Create your models here.

class TipoMascota(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Macota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoMascota,on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="mascotas",null=True)

    def __str__(self):
        return self.nombre
