from django.contrib import admin

from .models import Lector, Prestamo

admin.site.register(Prestamo)

admin.site.register(Lector)
