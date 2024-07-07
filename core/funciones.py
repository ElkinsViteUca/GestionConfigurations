from django.utils import timezone
import datetime
from django.db import models


class ModeloBase(models.Model):
    """ Modelo base para todos los modelos del proyecto """
    from django.contrib.auth.models import User
    #status = models.BooleanField(default=True)
    usuario_creacion = models.ForeignKey(User, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    usuario_modificacion = models.ForeignKey(User, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        usuario = None
        fecha_modificacion = timezone.now()

        if len(args):
            usuario = args[0].user.id

        for key, value in kwargs.items():
            if 'usuario_id' == key:
                usuario = value
            if 'fecha_modificacion' == key:
                fecha_modificacion = value

        if self.id:
            # Actualización: no modificar fecha de creación
            self.usuario_modificacion_id = usuario if usuario else 1
            self.fecha_modificacion = fecha_modificacion
        else:
            # Creación: establecer usuario y fecha de creación
            self.usuario_creacion_id = usuario if usuario else 1
            self.fecha_creacion = fecha_modificacion
            # Si se pasa 'fecha_creacion' como argumento, usarlo en lugar de 'fecha_modificacion'
            if 'fecha_creacion' in kwargs:
                self.fecha_creacion = kwargs['fecha_creacion']

        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     usuario = None
    #     fecha_modificacion = datetime.now()
    #     fecha_creacion = None
    #     if len(args):
    #         usuario = args[0].user.id
    #     for key, value in kwargs.items():
    #         if 'usuario_id' == key:
    #             usuario = value
    #         if 'fecha_modificacion' == key:
    #             fecha_modificacion = value
    #         if 'fecha_creacion' == key:
    #             fecha_creacion = value
    #     if self.id:
    #         self.usuario_modificacion_id = usuario if usuario else 1
    #         self.fecha_modificacion = fecha_modificacion
    #     else:
    #         self.usuario_creacion_id = usuario if usuario else 1
    #         self.fecha_creacion = fecha_modificacion
    #         if fecha_creacion:
    #             self.fecha_creacion = fecha_creacion
    #     models.Model.save(self)

    # class Meta:
    #     abstract = True
