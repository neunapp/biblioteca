from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(
        'prestamo/add/', 
        views.RegistrarPrestamo.as_view(), 
        name="prestamo_add"
    ),
]