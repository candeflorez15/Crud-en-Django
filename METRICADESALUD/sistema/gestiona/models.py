from statistics import mode
from django.db import models

# Create your models here.

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    saturacion = models.CharField(max_length=50)
    stress = models.CharField(max_length=10)

    def __str__(self):
        fila =  "Nombre: " + self.nombre + " - " + "Apellido: " + self.apellidos
        return fila

    def delete(self, using=None, keep_parents=False):
        self.delete
        super().delete()
