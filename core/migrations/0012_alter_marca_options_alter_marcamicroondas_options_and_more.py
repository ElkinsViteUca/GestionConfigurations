# Generated by Django 4.2.13 on 2024-07-07 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_televisor_resolucion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marca',
            options={'verbose_name': 'Marca de Televisor', 'verbose_name_plural': 'Marcas de Televisor'},
        ),
        migrations.AlterModelOptions(
            name='marcamicroondas',
            options={'verbose_name': 'Marca de Microonda', 'verbose_name_plural': 'Marcas de Microonda'},
        ),
        migrations.AlterModelOptions(
            name='marcarefri',
            options={'verbose_name': 'Marca de Refri', 'verbose_name_plural': 'Marcas de Refri'},
        ),
        migrations.AlterModelOptions(
            name='modelomicroondas',
            options={'verbose_name': 'Modelo de Microonda', 'verbose_name_plural': 'Modelo de Microondas'},
        ),
        migrations.AlterModelOptions(
            name='modelorefri',
            options={'verbose_name': 'Modelo de Refri', 'verbose_name_plural': 'Modelos de Refri'},
        ),
    ]
