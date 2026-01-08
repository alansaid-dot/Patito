from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Departamento
from applications.Persona.models import Empleado
from .forms import NewDepartamentoForm
from django.views.generic import (ListView)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name='departamentos'


class NewDepartamentoView(FormView):
    template_name = "departamento/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        depa = Departamento(
            nombre=form.cleaned_data['departamento'],
            subnombre=form.cleaned_data['short_name']
        )
        depa.save()

        #nombre = form.cleaned_data['nombre']
        #apellido = form.cleaned_data['apellidos']

        Empleado.objects.create(
            #first_name=nombre,
            #last_name=apellido,
            job='1',
            departamento=depa
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        print("ERRORES:", form.errors)
        return super().form_invalid(form)



# Create your views here.
