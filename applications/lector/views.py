from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView

# local apps
from .models import Prestamo, Lector
# forms
from .forms import PrestamoForm, MultiplePrestamoForm

class RegistrarPrestamo(FormView):
    template_name = "lector/add_prestamo.html"
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        # Prestamo.objects.create(
        #     lector=form.cleaned_data['lector'],
        #     libro=form.cleaned_data['libro'],
        #     fecha_prestamo=date.today(),
        #     devuelto=False
        # )
        #
        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )
        prestamo.save()

        libro = form.cleaned_data['libro']
        libro.stok = libro.stok - 1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)


class AddPrestamo(FormView):
    template_name = "lector/add_prestamo.html"
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        
        obj, created = Prestamo.objects.get_or_create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto = False,
            defaults={
                'fecha_prestamo': date.today()
            }
        )

        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')


class AddMultiplePrestamo(FormView):
    template_name = "lector/add_multiple_prestamo.html"
    form_class = MultiplePrestamoForm
    success_url = '.'

    def form_valid(self, form):
        #
        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros'])
        #
        prestamos = []
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector=form.cleaned_data['lector'],
                libro=l,
                fecha_prestamo=date.today(),
                devuelto=False
            )
            prestamos.append(prestamo)
        
        Prestamo.objects.bulk_create(
           prestamos 
        )
        

        return super(AddMultiplePrestamo, self).form_valid(form)

