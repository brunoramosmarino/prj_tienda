# Generated by Django 3.2.7 on 2021-09-29 16:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('precio', models.FloatField()),
                ('disponible', models.BooleanField()),
                ('imagen', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['categoria'],
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nivel', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nivel', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.IntegerField()),
                ('fecha_alta', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de alta')),
            ],
            options={
                'ordering': ['fecha_alta'],
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cp', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Localidades',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('num_doc', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='N° de documento')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nac', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='persona_localidad', to='tienda.localidad')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movimiento_cliente', to='tienda.cliente')),
            ],
            options={
                'ordering': ['fecha', 'numero'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_articulo', to='tienda.articulo')),
                ('movimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_movimiento', to='tienda.movimiento')),
            ],
            options={
                'ordering': ['articulo'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('legajo', models.AutoField(primary_key=True, serialize=False)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='empleado_cargo', to='tienda.cargo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleado_persona', to='tienda.persona')),
            ],
            options={
                'ordering': ['legajo'],
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cliente_persona', to='tienda.persona'),
        ),
    ]