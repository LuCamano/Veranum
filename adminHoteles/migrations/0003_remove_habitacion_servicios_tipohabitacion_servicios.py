# Generated by Django 5.0.6 on 2024-06-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminHoteles', '0002_habitacion_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='servicios',
        ),
        migrations.AddField(
            model_name='tipohabitacion',
            name='servicios',
            field=models.ManyToManyField(blank=True, to='adminHoteles.servicioadicional', verbose_name='Servicios Adicionales'),
        ),
    ]
