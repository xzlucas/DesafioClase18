from stat import FILE_ATTRIBUTE_DIRECTORY
from django.db import models

class Familiares(models.Model):
    nombre = models.CharField("nombre",max_length=20)
    apellido = models.CharField("apellido",max_length=20)
    fecha_nac = models.DateField("fecha_nac")
    DNI = models.IntegerField ("DNI")

