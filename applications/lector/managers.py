from django.db import models


class PrestamoManager(models.Manager):
    """ managers para el modelo Lector """

    def prestamo_all(self):

        resultado = self.filter.all()

        return resultado