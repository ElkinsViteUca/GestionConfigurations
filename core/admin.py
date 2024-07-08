from django.contrib import admin
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import modeloMicroondas,marcaMicroondas,Color, Vendedor,Pais,Provincia,Ciudad,Marca,Panel,Resolucion,MarcaRefri, ModeloRefri

# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Vendedor)
admin.site.register(Color)

#-------------------------Televisor--------------------------------
admin.site.register(Marca)

# class MarcaAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         try:
#             obj.save()
#         except IntegrityError as e:
#             self.message_user(request, f"Error: {e}", level='ERROR')
#             return False  # Indica que no se ha podido guardar el objeto
#
#         return True  # Indica que se ha guardado correctamente el objeto

admin.site.register(Panel)
admin.site.register(Resolucion)

#-------------------------Refrigeradora--------------------------------
admin.site.register(MarcaRefri)
admin.site.register(ModeloRefri)


#-------------------------Microondas--------------------------------
admin.site.register(marcaMicroondas)
admin.site.register(modeloMicroondas)