# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acceso(models.Model):
    idacceso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acceso'


class Atencion(models.Model):
    idatencion = models.IntegerField(primary_key=True)
    fechatencion = models.DateField(blank=True, null=True)
    idodontologo = models.ForeignKey('Odontologo', models.DO_NOTHING, db_column='idodontologo')
    idreserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='idreserva')

    class Meta:
        managed = False
        db_table = 'atencion'


class Boleta(models.Model):
    idboleta = models.IntegerField(primary_key=True)
    valortotal = models.IntegerField(blank=True, null=True)
    idatencion = models.ForeignKey(Atencion, models.DO_NOTHING, db_column='idatencion')
    iva = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleta'


class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True)
    nomcategoria = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'
# Unable to inspect table 'control_recepcion_pedido_producto'
# The error was: ORA-00942: table or view does not exist


class DetalleBoleta(models.Model):
    iddetalle = models.IntegerField(primary_key=True)
    idboleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='idboleta')
    idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='idservicio')
    valorservicio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_boleta'


class DetallePedido(models.Model):
    iddetalle = models.IntegerField(primary_key=True)
    idpedido = models.ForeignKey('Ordenpedido', models.DO_NOTHING, db_column='idpedido')
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto')
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class Empleado(models.Model):
    idempleado = models.IntegerField(primary_key=True)
    rut = models.ForeignKey('Persona', models.DO_NOTHING, db_column='rut')
    idtipoemp = models.ForeignKey('Tipoempleado', models.DO_NOTHING, db_column='idtipoemp')

    class Meta:
        managed = False
        db_table = 'empleado'


class Especialidad(models.Model):
    idespecialidad = models.IntegerField(primary_key=True)
    nomespecialidad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'


class EspecialidadOdontologo(models.Model):
    idespodontologo = models.IntegerField(primary_key=True)
    idespecialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='idespecialidad')
    idodontologo = models.ForeignKey('Odontologo', models.DO_NOTHING, db_column='idodontologo')

    class Meta:
        managed = False
        db_table = 'especialidad_odontologo'


class EstadoPedido(models.Model):
    idestadopedido = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    idpedido = models.ForeignKey('Ordenpedido', models.DO_NOTHING, db_column='idpedido')

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class EstadoRecepcion(models.Model):
    idestadorecepcion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_recepcion'


class EstadoReserva(models.Model):
    idestado = models.BooleanField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_reserva'


class Horareserva(models.Model):
    idhora = models.IntegerField(primary_key=True)
    fechadia = models.DateField(blank=True, null=True)
    hora = models.CharField(max_length=10, blank=True, null=True)
    vigente = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horareserva'


class Odontologo(models.Model):
    idodontologo = models.IntegerField(primary_key=True)
    rut = models.ForeignKey('Persona', models.DO_NOTHING, db_column='rut')

    class Meta:
        managed = False
        db_table = 'odontologo'


class Ordenpedido(models.Model):
    idpedido = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ordenpedido'


class Paciente(models.Model):
    idpaciente = models.IntegerField(primary_key=True)
    rut = models.ForeignKey('Persona', models.DO_NOTHING, db_column='rut')
    idtramoprevision = models.ForeignKey('TramoPrevision', models.DO_NOTHING, db_column='idtramoprevision')

    class Meta:
        managed = False
        db_table = 'paciente'


class Persona(models.Model):
    rut = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidopaterno = models.CharField(max_length=50, blank=True, null=True)
    apellidomaterno = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fechanac = models.DateField(blank=True, null=True)
    idtipoper = models.ForeignKey('Tipopersona', models.DO_NOTHING, db_column='idtipoper')
    vigente = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class Prevision(models.Model):
    idprevision = models.CharField(primary_key=True, max_length=1)
    nomprevision = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prevision'


class Producto(models.Model):
    idproducto = models.IntegerField(primary_key=True)
    nomproducto = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    vencimiento = models.DateField(blank=True, null=True)
    preciocompra = models.IntegerField(blank=True, null=True)
    precioventa = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    stockcritico = models.FloatField(blank=True, null=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor')
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.IntegerField(primary_key=True)
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')

    class Meta:
        managed = False
        db_table = 'proveedor'


class Reserva(models.Model):
    idreserva = models.IntegerField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    idpaciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='idpaciente')
    idespecialidad = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='idespecialidad')
    idhora = models.ForeignKey(Horareserva, models.DO_NOTHING, db_column='idhora')
    idestado = models.ForeignKey(EstadoReserva, models.DO_NOTHING, db_column='idestado')

    class Meta:
        managed = False
        db_table = 'reserva'


class Servicio(models.Model):
    idservicio = models.IntegerField(primary_key=True)
    idtiposervicio = models.ForeignKey('Tiposervicio', models.DO_NOTHING, db_column='idtiposervicio')
    nomservicio = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class ServicioProducto(models.Model):
    idproducto = models.OneToOneField(Producto, models.DO_NOTHING, db_column='idproducto', primary_key=True)
    idservicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='idservicio')

    class Meta:
        managed = False
        db_table = 'servicio_producto'
        unique_together = (('idproducto', 'idservicio'),)


class Tipoempleado(models.Model):
    idtipoemp = models.IntegerField(primary_key=True)
    nomtipoemp = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoempleado'


class Tipopersona(models.Model):
    idtipoper = models.BooleanField(primary_key=True)
    nomtipo = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipopersona'


class Tiposervicio(models.Model):
    idtiposervicio = models.IntegerField(primary_key=True)
    nomtipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiposervicio'


class TramoPrevision(models.Model):
    idtramoprevision = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    costo_pago = models.FloatField(blank=True, null=True)
    idprevision = models.ForeignKey(Prevision, models.DO_NOTHING, db_column='idprevision')

    class Meta:
        managed = False
        db_table = 'tramo_prevision'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Persona, models.DO_NOTHING, db_column='rut')
    clave = models.CharField(max_length=200)
    admin = models.BooleanField(blank=True, null=True)
    idacceso = models.ForeignKey(Acceso, models.DO_NOTHING, db_column='idacceso')

    class Meta:
        managed = False
        db_table = 'usuario'


