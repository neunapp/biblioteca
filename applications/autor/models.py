from django.db import models

# managers
from .managers import AutorManager

class Persona(models.Model):
    nombres = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionaldiad = models.CharField(
        max_length=20
    )
    edad = models.PositiveIntegerField()

    class Meta:
        abstract = True
    
    def __str__(self):
        return str(self.id) + '-' + self.nombres + '-' + self.apellidos



class Autor(Persona):

    objects = AutorManager()