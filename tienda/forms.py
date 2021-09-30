from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.forms.forms import Form
from .models import Localidad, Persona, Cliente, Movimiento, Cargo, Item, Empleado, Articulo
from dal import autocomplete


class DateInput(forms.DateInput):
    input_type = 'date'

class Localidad_form(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3 ','placeholder':'Nombre de la Localidad'}),
                   'cp': forms.TextInput(attrs={'type':'number','class':'form-control input shadow p-2 mb-3','placeholder':'Codigo postal de la Localidad'}),

        }


class Persona_form(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {'num_doc': forms.TextInput(attrs={'type':'number','class':'form-control input shadow p-2 mb-3 ','placeholder':'DNI de la persona'}),
                   'apellido': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3','placeholder':'Apellido de la persona'}),
                   'nombre': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3','placeholder':'Nombre de la persona'}),
                   'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input-sm shadow p-2 mb-3'}),
                   'localidad': forms.Select(attrs={'class':'form-control input shadow p-2 mb-3'}),
                   'direccion': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3','placeholder':'Lugar de recidencia'}),
                   'telefono': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3', 'placeholder':'Numero de contacto'}),
                   'email': forms.TextInput(attrs={'type':'email','class':'form-control input shadow p-2 mb-3', 'placeholder':'Email de la persona'})

                   

        }


class Cliente_form(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {'persona': autocomplete.ModelSelect2(url='persona_autocompletar',attrs={'class':'form-control input shadow p-2 mb-3'}),
                   'categoria': forms.TextInput(attrs={'type':'number','class':'form-control input shadow p-2 mb-3','placeholder':'Categoria del cliente'}),
                   'fecha_alta': DateInput(format='%Y-%m-%d', attrs={'class':'form-control input-sm shadow p-2 mb-3'}),
                   

        }


class Movimiento_form(ModelForm):
    class Meta:
        model = Movimiento
        fields = '__all__'
        widgets = {'tipo': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3', 'placeholder':'Tipo de movimiento'}),
                   'cliente': forms.Select(attrs={'class':'form-control input shadow p-2 mb-3'}),
                   'numero': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3','placeholder':'Numero de movimiento'}),
                   'fecha': DateInput(format='%Y-%m-%d', attrs=({'class':'form-control input shadow p-2 mb-3'}))
        }


class Articulo_form(ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__' 
        widgets = {'marca': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3', 'placeholder':'Marca del articulo'}),
                   'descripcion': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3', 'placeholder':'Descripcion del articulo'}),
                   'categoria': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3', 'placeholder':'Categoria del articulo'}),
                   'stock': forms.TextInput(attrs={'type':'number', 'class':'form-control input shadow p-2 mb-3', 'placeholder':'Cantidad disponible del articulo'}),
                   'precio': forms.TextInput(attrs={'type':'number', 'step':'.01', 'class':'form-control input shadow p-2 mb-3', 'placeholder':'Precio del articulo'}),
                   'disponible': forms.NullBooleanSelect(attrs={'class':'form-control input shadow p-2 mb-3'})

        }

class Cargo_form(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3', 'placeholder':'Nombre del cargo'}),
                   'nivel': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3', 'placeholder':'Nivel del cargoo'}),
                   'descripcion': forms.TextInput(attrs={'class':'form-control input shadow p-2 mb-3', 'placeholder':'Descripcion del cargo'}),

        }


class Item_form(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {'articulo': forms.Select(attrs={'class':'form-control input shadow p-2 mb-3'}),
                   'movimiento': forms.Select(attrs={'class':'form-control input shadow p-2 mb-3'}),
                   'cantidad': forms.TextInput(attrs={'type':'number', 'class':'form-control input shadow p-2 mb-3', 'placeholder':'Cantidad de items'}),

        }


class Empleado_form(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {'persona': forms.Select(attrs={'class':'form-control input shadow p-2 mb-3'}),
                   'cargo': forms.Select(attrs={'class':'form-control input shadow p-2 mb-3'}),

        }
