from django.db import models
from django.db.models.query_utils import Q
from core.funciones import ModeloBase
from djangoProject import settings

# Create your models here.
class Sexo(ModeloBase):
  nombre = models.CharField(default='',blank=False,null=True, max_length=100, verbose_name=u'Sexo')

  def __str__(self):
    return "{}".format(self.nombre)

  class Meta:
    verbose_name = u"Sexo"
    verbose_name_plural = u"Sexos"
    ordering = ['nombre']

  def save(self, *args, **kwargs):
    self.nombre = self.nombre.upper()
    super(Sexo, self).save(*args, **kwargs)

class Pais(ModeloBase):
  nombre = models.CharField(default='', max_length=100, verbose_name=u"Nombre")


  def __str__(self):
    return "{}".format(self.nombre)

  class Meta:
    verbose_name = u"País"
    verbose_name_plural = u"Paises"
    ordering = ['nombre']

  def en_uso(self):
    return self.provincia_set.values('id').all().exists()

  def save(self, *args, **kwargs):
    self.nombre = self.nombre.upper()
    super(Pais, self).save(*args, **kwargs)

class Provincia(ModeloBase):
  pais = models.ForeignKey(Pais, blank=False, null=True, verbose_name=u'País', on_delete=models.CASCADE)
  nombre = models.CharField(default='',blank=False,null=True, max_length=100, verbose_name=u"Nombre")


  def __str__(self):
    return "{} - {}".format(self.pais,self.nombre)

  class Meta:
    verbose_name = u"Provincia"
    verbose_name_plural = u"Provincias"
    ordering = ['nombre']
    unique_together = ('nombre', 'pais')

  def en_uso(self):
    return self.ciudad_set.values('id').all().exists()

  def save(self, *args, **kwargs):
    self.nombre = self.nombre.upper()
    super(Provincia, self).save(*args, **kwargs)

class Ciudad(ModeloBase):
  provincia = models.ForeignKey(Provincia, blank=False, null=True, verbose_name=u'Provincia', on_delete=models.CASCADE)
  nombre = models.CharField(default='',blank=False, null=True, max_length=100, verbose_name=u"Nombre")

  def __str__(self):
    return "{} - {}".format(self.provincia,self.nombre)

  class Meta:
    verbose_name = u"Canton"
    verbose_name_plural = u"Cantones"
    ordering = ['nombre']
    unique_together = ('nombre', 'provincia')


  def save(self, *args, **kwargs):
    self.nombre = self.nombre.upper()
    super(Ciudad, self).save(*args, **kwargs)

class Vendedor(ModeloBase):
  class TipoDocumento(models.IntegerChoices):
    NINGUNO = 0, "Ninguno"
    CEDULA = 1, "Cédula"
    PASAPORTE = 2, "Pasaporte"
    RUC = 3, "Ruc"

  tipodocumento = models.IntegerField(choices=TipoDocumento.choices, default=TipoDocumento.NINGUNO, blank=True, null=True,
                                      verbose_name=u"Tipo Documento")
  identificacion = models.CharField(default='', max_length=13, verbose_name=u"Identificación")
  nombre = models.CharField(default='', max_length=100, verbose_name=u'Nombres')
  apellido = models.CharField(default='', max_length=100, verbose_name=u"Apellidos")
  nacimiento = models.DateField(verbose_name=u"Fecha de nacimiento", null=True, blank=True)
  sexo = models.ForeignKey(Sexo, default=2, verbose_name=u'Sexo', on_delete=models.CASCADE)
  email = models.CharField(default='', max_length=200, verbose_name=u"Correo electronico personal")
  pais = models.ForeignKey(Pais, blank=False, null=True, verbose_name=u'País residencia', on_delete=models.SET_NULL)
  provincia = models.ForeignKey(Provincia, blank=False, null=True, verbose_name=u"Provincia de residencia", on_delete=models.SET_NULL)
  ciudad = models.ForeignKey(Ciudad, blank=False, null=True, verbose_name=u"Ciudad de residencia", on_delete=models.SET_NULL)
  direccion = models.CharField(default='', max_length=100, verbose_name=u"Calle principal", null=True, blank=True)
  celular = models.CharField(default='', max_length=50, verbose_name=u"Celular")
  #usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return '{} - {}'.format(self.apellido, self.nombre)

  class Meta:
    verbose_name = u"Vendedor"
    verbose_name_plural = u"Vendedores"
    ordering = ['apellido', 'nombre']
    unique_together = ('identificacion',)

#*******************************************Televisor*********************************************************
class Marca(ModeloBase):
  nombreMarca = models.CharField(default='',blank=False, null=True, max_length=100, unique=True, verbose_name='Marca')

  def __str__(self):
    return '{}'.format(self.nombreMarca)

  class Meta:
    verbose_name = u"Marca de Televisor"
    verbose_name_plural = u"Marcas de Televisor"
    ordering = ['nombreMarca']

  def save(self, *args, **kwargs):
    self.nombreMarca = self.nombreMarca.upper()
    super(Marca, self).save(*args, **kwargs)

class Panel(ModeloBase):
  nombrePanel = models.CharField(default='', blank=False, null=True,max_length=100, verbose_name=u'Panel')

  def __str__(self):
    return '{}'.format(self.nombrePanel)

  class Meta:
    verbose_name = u"Panel"
    verbose_name_plural = u"Paneles"
    unique_together = ('nombrePanel',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.nombrePanel = self.nombrePanel.upper()
    super(Panel, self).save(*args, **kwargs)

class Resolucion(ModeloBase):
  nombreResol = models.CharField(default='', blank=False, null=True,max_length=100, verbose_name=u'Resolución')

  def __str__(self):
    return u'%s' % self.nombreResol

  class Meta:
    verbose_name = u"Resolución"
    verbose_name_plural = u"Resoluciones"
    unique_together = ('nombreResol',)

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.nombreResol = self.nombreResol.upper()
    super(Resolucion, self).save(*args, **kwargs)

class Televisor(ModeloBase):
  nombretv = models.CharField(default='', max_length=50, verbose_name=u'Televisor')
  marca = models.ForeignKey(Marca,blank=False,null=True,default='', verbose_name=u'Marca',on_delete=models.SET_NULL)
  pulgadas = models.CharField(default='',blank=False,null=True, max_length=50, verbose_name=u'Pulgadas')
  tipoPanel = models.ForeignKey(Panel,blank=False,null=True, default='', verbose_name=u'Panel',on_delete=models.SET_NULL)
  resolucion = models.ForeignKey(Resolucion,blank=False,null=True,default='', max_length=50, verbose_name=u'Resolución',on_delete=models.SET_NULL)
  imagen = models.FileField("Foto", upload_to="core/televisores", blank=True, null=True)
  costo = models.DecimalField(default=0, blank=False,null=True,max_digits=7, decimal_places=2, verbose_name=u"Costo")
  stock = models.IntegerField(default=0,blank=False,null=True, verbose_name=u"Stock")
  estado = models.BooleanField(default=False)

  def get_image(self):
    if self.imagen:
      return '{}{}'.format(settings.MEDIA_URL, self.imagen)
    return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')
  pass

  def __str__(self):
    return '{}'.format(self.nombretv)

#******************************************** Refrigeradora ********************************************************
class MarcaRefri(ModeloBase):
  marcaRefri = models.CharField(default='',blank=False, null=True, max_length=100, verbose_name=u'Marca')

  def __str__(self):
    return '{}'.format(self.marcaRefri)

  class Meta:
    verbose_name = u"Marca de Refri"
    verbose_name_plural = u"Marcas de Refri"
    ordering = ['marcaRefri']

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.marcaRefri = self.marcaRefri.upper()
    super(MarcaRefri, self).save(*args, **kwargs)

class ModeloRefri(ModeloBase):
  modeloRefri = models.CharField(default='', blank=False, null=True,max_length=100, verbose_name=u'Modelo')

  def __str__(self):
    return '{}'.format(self.modeloRefri)

  class Meta:
    verbose_name = u"Modelo de Refri"
    verbose_name_plural = u"Modelos de Refri"
    ordering = ['modeloRefri']

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.modeloRefri = self.modeloRefri.upper()
    super(ModeloRefri, self).save(*args, **kwargs)

class Color(ModeloBase):
  color = models.CharField(default='',blank=False, null=True, max_length=100, verbose_name=u'Color')

  def __str__(self):
    return '{}'.format(self.color)

  class Meta:
    verbose_name = u"Color"
    verbose_name_plural = u"Colores"
    ordering = ['color']

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.color = self.color.upper()
    super(Color, self).save(*args, **kwargs)

class Refrigeradora(ModeloBase):
  nombrerefrigeradora = models.CharField(default='', max_length=50, verbose_name=u'Televisor')
  refrigeradoramarcaRefri = models.ForeignKey(MarcaRefri,blank=False, null=True, default='', verbose_name=u'Marca',on_delete=models.SET_NULL)
  refrigeradoramodeloRefri = models.ForeignKey(ModeloRefri,default='',blank=False, null=True, verbose_name=u'Modelo',on_delete=models.SET_NULL)
  capacidadLitros = models.IntegerField(default=0,verbose_name=u"Litros")
  dimensiones = models.CharField(default='0x0x0', max_length=50, verbose_name=u'Dimensiones altura*hancho*profundidad')
  refrigeradoraColor = models.ForeignKey(Color,blank=False, null=True, default='', verbose_name=u'Color',on_delete=models.SET_NULL)
  imagen = models.FileField("Foto", upload_to="core/refrigeradora", blank=True, null=True)
  costo = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name=u"Costo")
  stock = models.IntegerField(default=0,  verbose_name=u"Stock")
  estado = models.BooleanField(default=False)

  def get_image(self):
    if self.imagen:
      return '{}{}'.format(settings.MEDIA_URL, self.imagen)
    return '{}{}'.format(settings.STATIC_URL, 'static/img/default/empty.jpg')


#******************************************** Microondas ********************************************************

class marcaMicroondas(ModeloBase):
  marcaMicroondas = models.CharField(default='',blank=False, null=True, max_length=20, verbose_name=u'Marca')

  def __str__(self):
    return '{}'.format(self.marcaMicroondas)

  class Meta:
    verbose_name = u"Marca de Microonda"
    verbose_name_plural = u"Marcas de Microonda"
    ordering = ['marcaMicroondas']

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.color = self.marcaMicroondas.upper()
    super(marcaMicroondas, self).save(*args, **kwargs)


class modeloMicroondas(ModeloBase):
  modelo = models.CharField(default='', max_length=20, verbose_name=u'Modelo')

  def __str__(self):
    return '{}'.format(self.modelo)

  class Meta:
    verbose_name = u"Modelo de Microonda"
    verbose_name_plural = u"Modelo de Microondas"
    ordering = ['modelo']

  def en_uso(self):
    if self.item_set.values('id').filter(status=True).exists():
      return True
    return False

  def save(self, *args, **kwargs):
    self.color = self.modelo.upper()
    super(modeloMicroondas, self).save(*args, **kwargs)

class Microondas(ModeloBase):
  nombremicroondas = models.CharField(default='', max_length=20, verbose_name='Microondas')
  marcaMicroondas = models.ForeignKey(marcaMicroondas, blank=False, null=True, default='', verbose_name=u'Marca',
                                              on_delete=models.SET_NULL)
  modelo = models.ForeignKey(modeloMicroondas, default='', blank=False, null=True, verbose_name=u'Modelo',
                                               on_delete=models.SET_NULL)
  capacidad = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Capacidad")
  dimensiones = models.CharField(default='0x0x0', max_length=50, verbose_name=u'Dimensiones altura*hancho*profundidad')
  microondasColor = models.ForeignKey(Color, blank=False, null=True, default='', verbose_name=u'Color',
                                         on_delete=models.SET_NULL)
  imagen = models.FileField("Foto", upload_to="core/microondas", blank=True, null=True)
  costo = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name=u"Costo")
  stock = models.IntegerField(default=0, blank=True, null=True, verbose_name=u"Stock")
  estado = models.BooleanField(default=False)

  def get_image(self):
    if self.imagen:
      return '{}{}'.format(settings.MEDIA_URL, self.imagen)
    return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')
  pass
