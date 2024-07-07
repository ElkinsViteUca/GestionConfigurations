from django import forms
from django.forms import ModelForm
from django.forms import ValidationError

from core.models import *
class TelevisorForm(ModelForm):

  class Meta:
    model = Televisor
    #fields = ['nombretv','marca','pulgadas','tipoPanel','resolucion','imagen','costo','stock']
    fields = '__all__'
    widgets = {
      'nombretv': forms.TextInput(attrs={'placeholder':'Ingrese el Televisor'}),
      'marca': forms.Select(attrs={ 'placeholder': 'Seleccione la Marca','required': False}),
      'pulgadas': forms.TextInput(attrs={ 'placeholder': 'Ingrese las Pulgadas'}),
      'tipoPanel': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca','required': False}),
      'resolucion': forms.Select(attrs={ 'placeholder': 'Escoja la Resolución','required': False}),
      'imagen': forms.FileInput(attrs={ 'required': False}),
      'costo': forms.NumberInput(attrs={ 'required': False}),
      'stock': forms.NumberInput(attrs={ 'required': False})
    }

  def clean_costo(self):
    object = self.cleaned_data.get('costo')
    if object <= 0:
      raise forms.ValidationError("El precio debe ser mayor que cero.")
    return object

  def clean_nombretv(self):
    object = self.cleaned_data.get('nombretv')
    if not object.isalpha():
      raise forms.ValidationError("Recuerda ingresar sólo texto en el campo  {}.".format(nombre))
    return object

  def clean_pulgadas(self):
    object = self.cleaned_data.get('pulgadas')
    if not object.isnumeric():
      raise forms.ValidationError("Recuerad ingresar sólo datos numericos en {}.".format(object))

    if len(object)>2:
      raise forms.ValidationError("Recuerda ingresar sólo dos digitos en {}.".format(object))

    return object

  def clean_stock(self):
    object = self.cleaned_data.get('stock')
    if object <= 0:
      raise forms.ValidationError("Recuerda el stock debe ser mayor que 0 y tu tienes {}.".format(object))
    return object



class RefrigeradoraForm(ModelForm):

  class Meta:
    model = Refrigeradora
    #fields = '__all__'
    fields = ['nombrerefrigeradora','refrigeradoramarcaRefri','refrigeradoramodeloRefri','capacidadLitros',
              'dimensiones','refrigeradoraColor','imagen','costo','stock']
    widgets = {
      'nombrerefrigeradora': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la Refrigeradora'}),
      'refrigeradoramarcaRefri': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Marca'}),
      'refrigeradoramodeloRefri': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Modelo'}),
      'capacidadLitros': forms.NumberInput(attrs={'class': 'form-control', 'required': False, 'placeholder': 'Ingrese los Litros'}),
      'dimensiones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las Dimensiones'}),
      'refrigeradoraColor': forms.Select(attrs={'class': 'form-control'}),
      'imagen': forms.FileInput(attrs={'class': 'form-control', 'required': False}),
      'costo': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
      'stock': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),

    }



class MicroondasForm(ModelForm):
  class Meta:
    model = Microondas
    fields = '__all__'
    widgets = {
      'nombremicroondas': forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese el Nombre'}),
      'marcaMicroondas': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Marca'}),
      'modelo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Modelo'}),
      'capacidad': forms.NumberInput(
        attrs={'class': 'form-control', 'required': True, 'placeholder': 'Ingrese los Litros'}),
      'dimensiones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las Dimensiones'}),
      'microondasColor': forms.Select(attrs={'class': 'form-control'}),
      'imagen': forms.FileInput(attrs={'class': 'form-control', 'required': False}),
      'costo': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
      'stock': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
    }

