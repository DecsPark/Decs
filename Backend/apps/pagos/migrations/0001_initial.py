# Generated by Django 5.2.4 on 2025-07-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_salida', models.TextField(verbose_name='hora_salida')),
                ('pago_total', models.TextField(verbose_name='pago_total')),
                ('automovil_id', models.TextField(verbose_name='automovil_id')),
                ('factura', models.TextField(verbose_name='factura')),
            ],
        ),
    ]
