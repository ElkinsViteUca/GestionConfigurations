from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from core.models import *
from .forms import *
# Create your views here.

class televisorListView(ListView):
  template_name = "listadotv.html"
  context_object_name = 'Televisor'
  model = Televisor

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['titulo'] = "LISTA DE TELEVISORES"
    context['listar_url'] = '/listatelevisores/'
    context['crear_url'] = '/creartelevisores/'
    #context['pdf'] = '/pdfactivo/'
    context['query'] = self.request.GET.get("query")
    return context