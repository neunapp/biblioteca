from django.db import models
from django.db.models.signals import post_delete

# from autor
from applications.autor.models import Persona
# from local apps
from applications.libro.models import Libro
#
from .managers import PrestamoManager
from .signals import update_libro_stok

class Lector(Persona):
    
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(
        blank=True, 
        null=True
    )
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def save(self, *args, **kwargs):

        self.libro.stok = self.libro.stok - 1
        self.libro.save()

        super(Prestamo, self).save(*args, **kwargs)

    def __str__(self):
        return self.libro.titulo


# def update_libro_stok(sender, instance, **kwargs):
#     # actualizamos el stok si se elimina un prestamo
#     instance.libro.stok = instance.libro.stok + 1
#     instance.libro.save()

post_delete.connect(update_libro_stok, sender=Prestamo)