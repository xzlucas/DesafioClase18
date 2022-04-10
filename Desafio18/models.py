from django.db import models

# Create your models here.
from stat import FILE_ATTRIBUTE_DIRECTORY


class Familiares(models.Model):
    nombre = models.CharField("nombre",max_length=20)
    apellido = models.CharField("apellido",max_length=20)
    fecha_nac = models.DateField("fecha_nac")
    DNI = models.IntegerField ("DNI")

    def __str__(self) -> str:
        return f'{self.apellido}, {self.nombre}, DNI {self.DNI}'
