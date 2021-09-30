from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.query_utils import select_related_descend

class Localidad (models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.CharField(max_length=10)

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Localidades'
    
    def __str__(self):
        return '%s - %s' % (self.nombre, self.cp)


class Persona (models.Model):
    num_doc = models.CharField("N° de documento", max_length=20, primary_key=True)
    nombre = models.CharField("Nombre/s",max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField("Fecha de nacimiento", default=datetime.now)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=50, null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name='persona_localidad')
    telefono = models.CharField(max_length=20, null=True, blank=True)
    class Meta:
        ordering = ["apellido","nombre"]
    
    def __str__(self):
        return '%s - %s - %s' % (self.num_doc, self.apellido, self.nombre)


class Cliente (models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='cliente_persona')
    categoria = models.IntegerField()
    fecha_alta = models.DateField("Fecha de alta", default=datetime.now)
    
    class Meta:
        ordering = ["fecha_alta"]

    def __str__(self):
        return '%s - %s' % (self.persona.num_doc, self.categoria)


class Movimiento (models.Model):
    numero = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='movimiento_cliente')
    fecha = models.DateField(default=datetime.now)

    class Meta:
        ordering = ["fecha", "numero"]

    def __str__(self):
        return '%s - %s - %s' % (self.cliente.persona.num_doc, self.numero, self.tipo)



class Articulo (models.Model):
    marca = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=50)#hacer tabla de categorias
    stock = models.IntegerField()
    precio = models.FloatField()
    disponible = models.BooleanField()
    imagen = models.CharField(max_length=100, null=True, blank=True) 
    class Meta:
        ordering = ["categoria"]
    
    def __str__(self):
        return '%s - %s - %s - %s' % (self.categoria, self.marca, self.precio, self.stock)


        
class Item (models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.PROTECT, related_name='item_articulo')
    movimiento = models.ForeignKey(Movimiento, on_delete=models.PROTECT, related_name='item_movimiento')
    cantidad = models.IntegerField(default=1)
    class Meta:
        ordering = ["articulo"]
    
    def __str__(self):
        return '%s - %s - %s' % (self.articulo, self.movimietno, self.cantidad)


class Cargo (models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["nivel", "nombre"]
    
    def __str__(self):
        return '%s - %s' % (self.nombre, self.nivel)



class Empleado (models.Model):
    legajo = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='empleado_persona')
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='empleado_cargo')

    class Meta:
        ordering=["legajo"]

    def __str__(self):
        return '%s - %s - %s' % (self.persona.num_doc, self.cargo, self.legajo)

