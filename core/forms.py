from django import forms
from django.forms import ModelForm
from django.forms import ValidationError

from core.models import *
class TelevisorForm(ModelForm):

  class Meta:
    model = Televisor
    fields = '__all__'
    widgets = {
      'nombretv': forms.TextInput(attrs={'placeholder':'Ingrese el Televisor'}),
      'marca': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca'}),
      'pulgadas': forms.TextInput(attrs={ 'placeholder': 'Ingrese las Pulgadas'}),
      'tipoPanel': forms.Select(attrs={ 'placeholder': 'Ingrese la Marca'}),
      'resolucion': forms.TextInput(attrs={ 'placeholder': 'Ingrese las Pulgadas'}),
      'foto': forms.FileInput(attrs={ 'required': True}),
      'costo': forms.NumberInput(attrs={ 'required': True}),
      'stock': forms.NumberInput(attrs={ 'required': True}),

    }

class RefrigeradoraForm(ModelForm):

  class Meta:
    model = Refrigeradora
    fields = '__all__'
    widgets = {
      'nombrerefrigeradora': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la Refrigeradora'}),
      'refrigeradoramarcaRefri': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Marca'}),
      'refrigeradoramodeloRefri': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Modelo'}),
      'capacidadLitros': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Ingrese los Litros'}),
      'dimensiones': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las Dimensiones'}),
      'refrigeradoraColor': forms.Select(attrs={'class': 'form-control'}),
      'foto': forms.FileInput(attrs={'class': 'form-control', 'required': True}),
      'costo': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
      'stock': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),

    }

