# Generated by Django 4.2.13 on 2024-07-07 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_sexo_options_alter_pais_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ['nombreMarca'], 'verbose_name': 'Marca de Televisor', 'verbose_name_plural': 'Marcas de Televisor'},
        ),
        migrations.AlterField(
            model_name='marca',
            name='nombreMarca',
            field=models.CharField(default='', max_length=100, null=True, unique=True, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='panel',
            name='nombrePanel',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Panel'),
        ),
        migrations.AlterField(
            model_name='televisor',
            name='costo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Costo'),
        ),
        migrations.AlterField(
            model_name='televisor',
            name='pulgadas',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Pulgadas'),
        ),
        migrations.AlterField(
            model_name='televisor',
            name='resolucion',
            field=models.ForeignKey(default='', max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.resolucion', verbose_name='Resolución'),
        ),
        migrations.AlterField(
            model_name='televisor',
            name='stock',
            field=models.IntegerField(default=0, null=True, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='televisor',
            name='tipoPanel',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.panel', verbose_name='Panel'),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.ciudad', verbose_name='Ciudad de residencia'),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pais', verbose_name='País residencia'),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='provincia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.provincia', verbose_name='Provincia de residencia'),
        ),
    ]
