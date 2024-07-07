from django.contrib import admin
from .models import modeloMicroondas,marcaMicroondas,Color, Vendedor,Pais,Provincia,Ciudad,Marca,Panel,Resolucion,MarcaRefri, ModeloRefri

# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Vendedor)
admin.site.register(Color)

#-------------------------Televisor--------------------------------
admin.site.register(Marca)
admin.site.register(Panel)
admin.site.register(Resolucion)

#-------------------------Refrigeradora--------------------------------
admin.site.register(MarcaRefri)
admin.site.register(ModeloRefri)


#-------------------------Microondas--------------------------------
admin.site.register(marcaMicroondas)
admin.site.register(modeloMicroondas)