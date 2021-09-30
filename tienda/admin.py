from django.contrib import admin
from .models import *

my_models = [Localidad, Persona, Empleado, Cargo, Item, Articulo, Movimiento, Cliente]

admin.site.register(my_models)