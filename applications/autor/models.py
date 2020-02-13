from django.db import models

# managers
from .managers import AutorManager

class Autor(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionaldiad = models.CharField(
        max_length=30
    )
    edad = models.PositiveIntegerField()

    objects = AutorManager()

    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + self.apellidos