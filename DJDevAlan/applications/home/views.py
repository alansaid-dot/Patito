from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba

from .models import Prueba

from .forms import PruebaForm
from django.http import HttpResponse

def test_ok(request):
    return HttpResponse("Render está funcionando 🚀")

class indexView(TemplateView):
    template_name = 'home/Home/home.html'

class FoundationView(TemplateView):
    template_name='home/Home/foundation.html'

class PruebalistView(ListView):
    template_name = 'lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "pruebas.html" 
    context_object_name = 'lista_prueba' 
    
class PruebaCreateView(CreateView):
    template_name = 'home/Home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url='/'