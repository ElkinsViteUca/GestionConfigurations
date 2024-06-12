from django.contrib import admin
from .models import Vendedor,Pais,Provincia,Ciudad

# Register your models here.
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Provincia)
admin.site.register(Vendedor)