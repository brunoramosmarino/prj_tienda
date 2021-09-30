from django.shortcuts import render, redirect
from .models import Articulo, Cliente, Item, Movimiento, Persona, Cargo, Empleado
from .forms import Articulo_form, Cliente_form, Localidad_form, Movimiento_form, Persona_form, Cargo_form, Item_form, Empleado_form, Localidad
from django.db.models.deletion import ProtectedError
from dal import autocomplete
from django.db.models import Q


class PersonaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Persona.objects.none()

        qs = Persona.objects.all()

        if self.q:
            qs = qs.filter(num_doc__icontains=self.num_doc)

        return qs


def menu(request, template_name='tienda/menu.html'):
    return render(request, template_name)


def localidad_listar (request, template_name='tienda/localidades.html'):
    localidades = Localidad.objects.all()
    dato_localidad = {"localidades" : localidades}
    return render(request, template_name, dato_localidad)


def persona_listar (request, template_name='tienda/personas.html'):
    personas = Persona.objects.all()
    dato_persona = {"personas" : personas}
    return render(request, template_name, dato_persona)


def cliente_listar(request, template_name='tienda/clientes.html'):
    clientes = Cliente.objects.all()
    dato_cliente = {"clientes" : clientes}
    return render(request, template_name, dato_cliente)


def movimiento_listar(request, template_name='tienda/movimientos.html'):
    movimientos = Movimiento.objects.all()
    dato_movimiento = {"movimientos" : movimientos}
    return render(request, template_name, dato_movimiento) 


def articulo_listar(request, template_name='tienda/articulos.html'):
    articulos = Articulo.objects.all()
    dato_articulo = {"articulos" : articulos}
    return render(request, template_name, dato_articulo)


def item_listar(request, template_name='tienda/items.html'):
    items = Item.objects.all()
    dato_item = {"items" : items}
    return render(request, template_name, dato_item) 


def cargo_listar(request, template_name='tienda/cargos.html'):
    cargos = Cargo.objects.all()
    dato_cargo = {"cargos" : cargos}
    return render(request, template_name, dato_cargo)


def empleado_listar(request, template_name='tienda/empleados.html'):
    empleados = Empleado.objects.all()
    dato_empleado = {"empleados" : empleados}
    return render(request, template_name, dato_empleado)


def nueva_localidad(request, template_name='tienda/localidad_form.html'):
    if request.method=='POST':
        form = Localidad_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidad_listar')
        else:
            print(form.errors)
    else:
        form = Localidad_form()
    dato = {'form':form}
    return render(request, template_name, dato)


def modificar_localidad(request, pk, template_name='tienda/localidad_form.html'):
    localidad = Localidad.objects.get(pk = pk)
    form = Localidad_form(request.POST or None, instance = localidad)
    if form.is_valid():
        form.save(commit = True)
        return redirect('localidad_listar')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)


def eliminar_localidad(request, pk, template_name='tienda/persona_confirmar_eliminacion.html'):
    localidad = Localidad.objects.get(pk = pk)
    if request.method=='POST':
        try:
            localidad.delete()
        except ProtectedError:
            print("La Localidad esta protegida")
        return redirect('localidad_listar')
    else:
        dato = {'form':localidad}
        return render(request, template_name, dato)


def nueva_persona(request, template_name='tienda/persona_form.html'):
    if request.method=='POST':
        form = Persona_form(request.POST)
        if form.is_valid():
            print("hola")
            form.save(commit=True)
            return redirect('persona_listar')
        else:
            print(form.errors)
    else:
        print("no entro")
        form = Persona_form()
    dato = {"form":form,'pk':True}
    return render(request, template_name, dato)


def modificar_persona(request, pk, template_name='tienda/persona_form.html'):
    persona = Persona.objects.get(num_doc = pk)
    form = Persona_form(request.POST or None, instance = persona)
    if form.is_valid():
        form.save(commit = True)
        return redirect('persona_listar')
    else:
        print(form.errors)
    datos = {'form':form, 'pk':False}
    return render(request, template_name, datos)


def eliminar_persona(request, pk, template_name='tienda/persona_confirmar_eliminacion.html'):
    persona = Persona.objects.get(num_doc = pk)
    if request.method=='POST':
        try:
            persona.delete()
        except ProtectedError:
            print("esta persona esta protegida")
            
        return redirect('persona_listar')
    else:
        dato = {"form":persona}
        return render(request, template_name, dato)


def nuevo_cliente(request, template_name='tienda/cliente_form.html'):
    if request.method=='POST':
        form = Cliente_form(request.POST)
        if form.is_valid():
            print("hola")
            form.save(commit=True)
            return redirect('cliente_listar')
        else:
            print(form.errors)
    else:
        print("no entro")
        form = Cliente_form()
    dato = {"form":form}
    return render(request, template_name, dato)


def modificar_cliente(request, pk, template_name='tienda/cliente_form.html'):
    cliente = Cliente.objects.get(pk = pk)
    form = Cliente_form(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save(commit = True)
        return redirect('cliente_listar')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)


def eliminar_cliente(request, pk, template_name='tienda/persona_confirmar_eliminacion.html'):
    cliente = Cliente.objects.get(pk = pk)
    if request.method=='POST':
        try:
            cliente.delete()
        except ProtectedError:
            print("este cleitne esta protegido")
            
        return redirect('cliente_listar')
    else:
        dato = {"form":cliente}
        return render(request, template_name, dato)



def nuevo_movimiento(request, template_name='tienda/movimiento_form.html'):
    if request.method=='POST':
        form = Movimiento_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('movimiento_listar')
        else:
            print (form.errors)
    else:
        form = Movimiento_form()
    dato = {"form":form}
    return render(request, template_name, dato)


def modificar_movimiento(request, pk, template_name='tienda/movimiento_form.html'):
    movimiento = Movimiento.objects.get(pk = pk)
    form = Movimiento_form(request.POST or None, instance = movimiento)
    if form.is_valid():
        form.save(commit=True)
        return redirect('movimiento_listar')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)


def eliminar_movimiento(request, pk, template_name='tienda/persona_confirmar_eliminacion.html'):
    movimiento = Movimiento.objects.get(pk = pk)
    if request.method=='POST':
        try:
            movimiento.delete()
        except ProtectedError:
            print("Este movimiento esta protegido")
        return redirect('movimiento_listar')
    else:
        dato = {'form':movimiento}
        return render(request, template_name, dato)


def nuevo_articulo(request, template_name='tienda/articulo_form.html'):
    if request.method=='POST':
        form = Articulo_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('articulo_listar')
        else:
            print(form.errors)
    else:
        form = Articulo_form()
    dato = {'form':form}
    return render(request, template_name, dato)


def modificar_articulo(request, pk, template_name='tienda/articulo_form.html'):
    articulo = Articulo.objects.get(pk = pk)
    form = Articulo_form(request.POST or None, instance = articulo)
    if form.is_valid():
        form.save(commit = True)
        return redirect('articulo_listar')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)


def eliminar_articulo(request, pk, template_name='tienda/persona_confirmar_eliminacion.html'):
    articulo = Articulo.objects.get(pk = pk)
    if request.method=='POST':
        try:
            articulo.delete()
        except ProtectedError:
            print("El articulo esta protegido")
        return redirect('articulo_listar')
    else:
        dato = {'form':articulo}
        return render(request, template_name, dato)


def nuevo_cargo(request, template_name='tienda/cargo_form.html'):
    if request.method=='POST':
        form = Cargo_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('cargo_listar')
        else:
            print(form.errors)
    else:
        form = Cargo_form()
    dato = {'form':form}
    return render(request, template_name, dato)


def modificar_cargo(request, pk, template_name='tienda/cargo_form.html'):
    cargo = Cargo.objects.get(pk = pk)
    form = Cargo_form(request.POST or None, instance = cargo)
    if form.is_valid():
        form.save(commit = True)
        return redirect('cargo_listar')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)


def eliminar_cargo(request, pk, template_name='tienda/persona_confirmar_eliminacion.html'):
    cargo = Cargo.objects.get(pk = pk)
    if request.method=='POST':
        try:
            cargo.delete()
        except ProtectedError:
            print("El cargo esta protegido")
        return redirect('cargo_listar')
    else:
        dato = {'form':cargo}
        return render(request, template_name, dato)


def nuevo_item(request, template_name='tienda/item_form.html'):
    if request.method=='POST':
        form = Item_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('item_listar')
        else:
            print(form.errors)
    else:
        form = Item_form()
    dato = {'form':form}
    return render(request, template_name, dato)


def modificar_item(request, pk, template_name='tienda/item_form.html'):
    item = Item.objects.get(pk = pk)
    form = Item_form(request.POST or None, instance = item)
    if form.is_valid():
        form.save(commit = True)
        return redirect('item_listar')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)


def eliminar_item(request, pk, template_name='tienda/persona_confirmar_eliminacion.html'):
    item = Item.objects.get(pk = pk)
    if request.method=='POST':
        try:
            item.delete()
        except ProtectedError:
            print("El item esta protegido")
        return redirect('item_listar')
    else:
        dato = {'form':item}
        return render(request, template_name, dato)


def nuevo_empleado(request, template_name='tienda/empleado_form.html'):
    if request.method=='POST':
        form = Empleado_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('empleado_listar')
        else:
            print(form.errors)
    else:
        form = Empleado_form()
    dato = {'form':form}
    return render(request, template_name, dato)


def modificar_empleado(request, pk, template_name='tienda/empleado_form.html'):
    empleado = Empleado.objects.get(pk = pk)
    form = Empleado_form(request.POST or None, instance = empleado)
    if form.is_valid():
        form.save(commit = True)
        return redirect('empleado_listar')
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request, template_name, datos)


def eliminar_empleado(request, pk, template_name='tienda/persona_confirmar_eliminacion.html'):
    empleado = Empleado.objects.get(pk = pk)
    if request.method=='POST':
        try:
            empleado.delete()
        except ProtectedError:
            print("El empleado esta protegido")
        return redirect('empleado_listar')
    else:
        dato = {'form':empleado}
        return render(request, template_name, dato)