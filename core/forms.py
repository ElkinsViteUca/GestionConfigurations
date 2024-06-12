from django import forms
from django.forms import ModelForm
from django.forms import ValidationError

from core.models import *
class TelevisorForm(ModelForm):

  class Meta:
    model = Televisor
    fields = '__all__'
    widgets = {
      'nombretv': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el Televisor'}),
      'marca': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Marca'}),
      'pulgadas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las Pulgadas'}),
      'tipoPanel': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Marca'}),
      'resolucion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las Pulgadas'}),
      'foto': forms.FileInput(attrs={'class': 'form-control', 'required': True}),
      'costo': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
      'stock': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),

    }