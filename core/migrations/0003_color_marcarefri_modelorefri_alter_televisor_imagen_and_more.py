# Generated by Django 4.2.13 on 2024-06-13 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_marca_panel_televisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('color', models.CharField(default='', max_length=100, verbose_name='Color')),
                ('usuario_creacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colores',
                'unique_together': {('color',)},
            },
        ),
        migrations.CreateModel(
            name='MarcaRefri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('marcaRefri', models.CharField(default='', max_length=100, verbose_name='Marca')),
                ('usuario_creacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'unique_together': {('marcaRefri',)},
            },
        ),
        migrations.CreateModel(
            name='ModeloRefri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('modeloRefri', models.CharField(default='', max_length=100, verbose_name='Modelo')),
                ('usuario_creacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'unique_together': {('modeloRefri',)},
            },
        ),
        migrations.AlterField(
            model_name='televisor',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='core/televisores', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='televisor',
            name='marca',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.marca', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='televisor',
            name='tipoPanel',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.panel', verbose_name='Panel'),
        ),
        migrations.CreateModel(
            name='Refrigeradora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('nombrerefrigeradora', models.CharField(default='', max_length=50, verbose_name='Televisor')),
                ('capacidadLitros', models.IntegerField(blank=True, default=0, null=True, verbose_name='Litros')),
                ('dimensiones', models.CharField(default='0x0x0', max_length=50, verbose_name='Dimensiones altura*hancho*profundidad')),
                ('imagen', models.FileField(blank=True, null=True, upload_to='core/refrigeradora', verbose_name='Foto')),
                ('costo', models.DecimalField(decimal_places=4, default=0, max_digits=30, verbose_name='Costo')),
                ('stock', models.IntegerField(blank=True, default=0, null=True, verbose_name='Stock')),
                ('refrigeradoraColor', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.color', verbose_name='Color')),
                ('refrigeradoramarcaRefri', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.marcarefri', verbose_name='Marca')),
                ('refrigeradoramodeloRefri', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.modelorefri', verbose_name='Modelo')),
                ('usuario_creacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
