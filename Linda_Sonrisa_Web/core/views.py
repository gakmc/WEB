from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
# from core.forms import formLog
from django.contrib.auth import login, authenticate
from .models import Reserva, Producto, Usuario,Acceso,Persona,Paciente
# from .forms import ReservaForm, ProductosForm
# from forms import LoginForm
from django.db import connection

# Create your views here.


def home(request):
    return render(request, 'core/home.html')



@login_required
def reserva(request):
    return render(request, 'core/reserva.html')


def nosotros(request):
    return render(request, 'core/nosotros.html')


@login_required
def nueva_reserva(request):
    return render(request, 'core/nueva_reserva.html')


# Producto
def Lista_Productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("MOSTRARPRODUCTO", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def productos_list(request):
    data = {
        'product_list': Lista_Productos()
    }
    return render(request, 'core/productos_list.html', data)


def productos_form(request):
    data = {
        'categoria': Combo_Categorias(),
        'proveedor': Combo_Proveedor(),
    }

    if request.method == 'POST':
        idcategoria = request.POST.get('categoria')
        idproveedor = request.POST.get('prov')
        nomproducto = request.POST.get('nombre')
        vencimiento = request.POST.get('fecha')
        marca = request.POST.get('marca')
        preciocompra = request.POST.get('precom')
        precioventa = request.POST.get('preven')
        stock = request.POST.get('stock')
        stockcritico = request.POST.get('stockcri')
        descripcion = request.POST.get('desc')
        agregar_producto(idcategoria, idproveedor, nomproducto, vencimiento,
                         marca, preciocompra, precioventa, stock, stockcritico, descripcion)
        data['mensaje'] = 'Agregado Correctamente'

    return render(request, 'core/productos_form.html', data)

# def productos_eliminar(request):


def Combo_Categorias():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("COMBOCATEGORIA", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def Combo_Proveedor():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("COMBOPROVEEDOR", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def agregar_producto(idcategoria, idproveedor, nomproducto, vencimiento, marca, preciocompra, precioventa, stock, stockcritico, descripcion):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("SET_PRODUCTOAGREGA", [idcategoria, idproveedor, nomproducto,
                                           vencimiento, marca, preciocompra, precioventa, stock, stockcritico, descripcion])


# Registro de paciente

def registro(request):
    data = {
        'prevision': Combo_Prev(),
        # 'tramo': Combo_Anidado(),
    }

    if request.method == 'POST':
        userna = request.POST.get('user')
        passw = request.POST.get('pass')
        rut = request.POST.get('rut')
        nom = request.POST.get('nom')
        apep = request.POST.get('apepa')
        apem = request.POST.get('apema')
        mail = request.POST.get('mail')
        sex = request.POST.get('sex')
        cel = request.POST.get('fono')
        fecnac = request.POST.get('fecnac')
        prev = request.POST.get('tipoprev')
        registro_paciente(userna, passw, rut, nom, apep,
                          apem, mail, sex, cel, fecnac, prev)
    else:
        data["message"] = "No se pudo completar el registro, favor valide que sus datos sean correctos e intentelo de nuevamente."

    return render(request, 'registration/registro.html', data)


def registro_paciente(userna, passw, rut, nom, apep, apem, mail, sex, cel, fecnac, prev):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("REGISTROPACIENTE", [
                    userna, passw, rut, nom, apep, apem, mail, sex, cel, fecnac, prev])


def Combo_Prev():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("COMBOPREV", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def Combo_TramoPrev():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("COMBOLETRAPREV", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def Combo_Anidado(idprevision):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("COMBOTRAMO_DJANGO", [out_cur, idprevision])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def comboboxanidado(request):
    prevision = request.GET.get('prevision')
    data = {
        'tramo': Combo_Anidado(prevision)
    }

    return render(request, 'core/combobox_anidado.html', data)


def Lista_Reservas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("MOSTRARRESERVA", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def reserva_list(request):
    data = {
        'reservas': Lista_Reservas()
    }
    return render(request, 'core/reservas_pacientes.html', data)