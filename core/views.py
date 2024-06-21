from urllib import request

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from core.models import *
from .forms import *
# Create your views here.


class InicioTemplateView(TemplateView):
  template_name = "Administrador/cardsAdministrador.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "Administrador"
    return context

class televisorListView(ListView):
  template_name = "formularios/listadotv.html"
  context_object_name = 'Televisor'
  model = Televisor

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "LISTA DE TELEVISORES"
    context['boton'] = "Crear Registro"
    context['listar_url'] = '/listatelevisores/'
    context['crear_url'] = '/creartelevisores/'
    #context['pdf'] = '/pdfactivo/'
    context['query'] = self.request.GET.get("query")
    return context



class televisorCreateView(CreateView):
    template_name = 'formularios/formulariotvPrueba.html'
    model = Televisor
    form_class = TelevisorForm
    success_url = reverse_lazy('listatelevisores')

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['titulo'] = "CREAR REGISTRO TV"
      context['boton'] = "Guardar Registro"
      context['listar_url'] = '/listaempleado/'
      context['action_save'] = '/creartelevisores/'
      context['form_title'] = 'Formulario TV'
      return context

#     def post(self,request,*args ,**kwargs):
#       print(request.POST)
#       return redirect('listatelevisores')

class actualizarTelevisor(UpdateView):
  model = Televisor
  template_name = "formularios/formulariotvPrueba.html"
  success_url = reverse_lazy('listatelevisores')
  form_class = TelevisorForm
  #queryset = Televisor.objects.get(pk=request.GET.get("id"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['action_save'] = self.request.path
    context['titulo'] = 'Administrador'
    context['form_title'] = 'ACTUALIZAR REGISTRO TV'
    context['listar_url'] = '/listatelevisores'
    context['boton'] = "Actualizar"
    context['table_title'] = 'Listado TV'
    return context

  class eliminarTelevisor(DeleteView):
    model = Televisor
    template_name = "arita/deleteArea.html"
    success_url = reverse_lazy('listatelevisores')

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['action_save'] = self.request.path
      context['titulo'] = 'ELMINACIÓN DE AREA'
      context['listar_url'] = '/listatelevisores'
      context['boton'] = "Eliminar"
      return context


#******************************************** Refrigeradora ********************************************************
class refrigeradoraListView(ListView):
  template_name = "listadoRefri.html"
  context_object_name = 'Refrigeradora'
  model = Televisor

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "LISTA DE REFRIGERADORAS"
    context['listar_url'] = '/listarefrigeradoras/'
    context['crear_url'] = '/crearrefrigeradoras/'
    #context['pdf'] = '/pdfactivo/'
    context['query'] = self.request.GET.get("query")
    return context