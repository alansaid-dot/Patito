from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from django.db.models import Q
from .models import Empleado, Habilidades
from .forms import EmpleadoForm, HabilidadForm
import os
from django.http import HttpResponse

def debug_view(request):
    return HttpResponse(str(os.listdir('/opt/render/project/src/DJDevAlan')))

class InicioView(TemplateView):
    """Vista de carga página de inicio"""
    template_name='inicio.html'
    
class ListaEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by= 10
    ordering='first_name'
    context_object_name='empleados'
    model=Empleado

class LisAllEmpleados(ListView):
    template_name = 'persona/lis_all.html' 
    paginate_by = 4
    ordering = 'first_name'
    context_object_name='empleados'
    
    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword", '')
        #print('===================', palabra_clave)
        lista = Empleado.objects.filter(
            Q(first_name__icontains=palabra_clave) |
            Q(last_name__icontains=palabra_clave)
        )
        return lista


class ListByAreaEmpleado(ListView):
    template_name='persona/list_by_area.html'
    context_object_name='empleados'
    
    def get_queryset(self):
        area=self.kwargs['subnombre']
        lista=Empleado.objects.filter(
        departamento__subnombre=area
        )
        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name='persona/habilidades.html'
    context_object_name='habilidades'
    
    def get_queryset(self):
        empleado=Empleado.objects.get(id=2)
        return empleado.Habilidades.all()


    
class listEmpleadoByKword(ListView):
    template_name='persona/by_kword.html'
    context_object_name='empleados'
    
    def get_queryset(self):
        print('*********************')
        palabra_clave=self.request.GET.get("kword", '')
        #print('===================', palabra_clave)
        lista=Empleado.objects.filter(first_name=palabra_clave)
        return lista
    

class EmpleadosDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadosDetailView, self).get_context_data(**kwargs)
        context["titulo"]='Empleado del mes'
        return context
    

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class= EmpleadoForm
    success_url=reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self, form):
        empleado=form.save(commit=False)
        empleado.full_name=empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = "persona/success.html"
    
class EmpleadoUpdateView(UpdateView):
    template_name='persona/update.html'
    model=Empleado
    fields=[
        'first_name',
        'last_name',
        'full_name',
        'job',
        'departamento',
        'Habilidades'
    ]
    success_url=reverse_lazy('persona_app:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        print('######################### TODO POST ########################3')
        print(request.POST)
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        self.object=form.save()
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model=Empleado
    template_name='persona/delete.html'
    success_url=reverse_lazy('persona_app:empleados_admin')
    
class HabilidadCreateView(CreateView):
    """Vista para crear nuevas habilidades"""
    template_name = 'persona/add_habilidad.html'
    form_class = HabilidadForm
    success_url = reverse_lazy('persona_app:lista_habilidades')
    
    def form_valid(self, form):
        # Opcional: puedes añadir lógica adicional aquí
        return super(HabilidadCreateView, self).form_valid(form)

class ListaHabilidadesView(ListView):
    """Vista para listar todas las habilidades"""
    template_name = 'persona/lista_habilidades.html'
    model = Habilidades
    context_object_name = 'habilidades'
    ordering = 'habilidad'
    paginate_by = 10

class HabilidadUpdateView(UpdateView):
    """Vista para actualizar habilidades"""
    template_name = 'persona/update_habilidad.html'
    model = Habilidades
    fields = ['habilidad']
    success_url = reverse_lazy('persona_app:lista_habilidades')

class HabilidadDeleteView(DeleteView):
    """Vista para eliminar habilidades"""
    model = Habilidades
    template_name = 'persona/delete_habilidad.html'
    success_url = reverse_lazy('persona_app:lista_habilidades')
    