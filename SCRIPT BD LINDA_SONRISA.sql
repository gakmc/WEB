--Crear Usuario

Create user C##WEB
identified by "sys"
default tablespace USERS
temporary tablespace TEMP
profile DEFAULT
quota 3m on users;

GRANT "RESOURCE" TO C##WEB;
GRANT "CONNECT" TO C##WEB;
grant create procedure to C##WEB;
grant create sequence to C##WEB;
grant create session to C##WEB;
grant create synonym to C##WEB;
grant create table to C##WEB;
grant create view to C##WEB;
GRANT UNLIMITED TABLESPACE TO C##WEB;
/

CREATE TABLE acceso (
    idacceso      NUMBER(2) NOT NULL,
    nombre        VARCHAR2(100),
    descripcion   VARCHAR2(300)
);

ALTER TABLE acceso ADD CONSTRAINT acceso_pk PRIMARY KEY ( idacceso );

CREATE TABLE atencion (
    idatencion     NUMBER(10) NOT NULL,
    fechatencion   DATE,
    idodontologo   NUMBER(10) NOT NULL,
    idreserva      NUMBER(10) NOT NULL
);

CREATE UNIQUE INDEX atencion__idx ON
    atencion (
        idreserva
    ASC );

ALTER TABLE atencion ADD CONSTRAINT atencion_pk PRIMARY KEY ( idatencion );

CREATE TABLE boleta (
    idboleta     NUMBER(10) NOT NULL,
    valortotal   NUMBER(10),
    idatencion   NUMBER(10) NOT NULL,
    iva          NUMBER(10)
);

CREATE UNIQUE INDEX boleta__idx ON
    boleta (
        idatencion
    ASC );

ALTER TABLE boleta ADD CONSTRAINT boleta_pk PRIMARY KEY ( idboleta );

--  ERROR: Table name length exceeds maximum allowed length(30) 
CREATE TABLE control_recepcion_pedido_producto (
    idcontrol           NUMBER(10) NOT NULL,
    fecharecepcion      DATE,
    observaciones       VARCHAR2(1000 CHAR),
    idestadorecepcion   NUMBER(2) NOT NULL,
    idpedido            NUMBER(10) NOT NULL
);

--  ERROR: Index name length exceeds maximum allowed length(30) 

CREATE UNIQUE INDEX control_recepcion_pedido_producto__idx ON
    control_recepcion_pedido_producto (
        idpedido
    ASC );

--  ERROR: PK name length exceeds maximum allowed length(30) 
ALTER TABLE control_recepcion_pedido_producto ADD CONSTRAINT control_recepcion_pedido_producto_pk PRIMARY KEY ( idcontrol );

CREATE TABLE detalle_boleta (
    iddetalle       NUMBER(10) NOT NULL,
    idboleta        NUMBER(10) NOT NULL,
    idservicio      NUMBER(5) NOT NULL,
    valorservicio   NUMBER(10)
);

ALTER TABLE detalle_boleta ADD CONSTRAINT detalle_boleta_pk PRIMARY KEY ( iddetalle );

CREATE TABLE detalle_pedido (
    iddetalle    NUMBER(10) NOT NULL,
    idpedido     NUMBER(10) NOT NULL,
    idproducto   NUMBER(10) NOT NULL,
    cantidad     NUMBER(5)
);

ALTER TABLE detalle_pedido ADD CONSTRAINT detalle_pedido_pk PRIMARY KEY ( iddetalle );

CREATE TABLE empleado (
    idempleado   NUMBER(10) NOT NULL,
    rut          VARCHAR2(15 CHAR) NOT NULL,
    idtipoemp    NUMBER(5) NOT NULL
);

CREATE UNIQUE INDEX empleado__idx ON
    empleado (
        rut
    ASC );

ALTER TABLE empleado ADD CONSTRAINT empleado_pk PRIMARY KEY ( idempleado );

CREATE TABLE especialidad (
    idespecialidad    NUMBER(10) NOT NULL,
    nomespecialidad   VARCHAR2(100 CHAR)
);

ALTER TABLE especialidad ADD CONSTRAINT especialidad_pk PRIMARY KEY ( idespecialidad );

CREATE TABLE especialidad_odontologo (
    idespodontologo NUMBER(10) NOT NULL,
    idespecialidad   NUMBER(10) NOT NULL,
    idodontologo     NUMBER(10) NOT NULL
);

ALTER TABLE especialidad_odontologo ADD CONSTRAINT idespodontologo_pk PRIMARY KEY ( idespodontologo );

CREATE TABLE estado_pedido (
    idestadopedido   NUMBER(2) NOT NULL,
    descripcion      VARCHAR2(200),
    idpedido         NUMBER(10) NOT NULL
);

ALTER TABLE estado_pedido ADD CONSTRAINT estado_pedido_pk PRIMARY KEY ( idestadopedido );

CREATE TABLE estado_recepcion (
    idestadorecepcion   NUMBER(2) NOT NULL,
    descripcion         VARCHAR2(200)
);

ALTER TABLE estado_recepcion ADD CONSTRAINT estado_recepcion_pk PRIMARY KEY ( idestadorecepcion );

CREATE TABLE estado_reserva (
    idestado      NUMBER(1) NOT NULL,
    nombre        VARCHAR2(50),
    descripcion   VARCHAR2(100)
);

ALTER TABLE estado_reserva ADD CONSTRAINT estado_reserva_pk PRIMARY KEY ( idestado );

CREATE TABLE horareserva (
    idhora     NUMBER(10) NOT NULL,
    fechadia   DATE,
    hora       VARCHAR2(10 CHAR),
    vigente    NUMBER(1)
);

ALTER TABLE horareserva ADD CONSTRAINT horareserva_pk PRIMARY KEY ( idhora );

CREATE TABLE odontologo (
    idodontologo   NUMBER(10) NOT NULL,
    rut            VARCHAR2(15 CHAR) NOT NULL
);

CREATE UNIQUE INDEX odontologo__idx ON
    odontologo (
        rut
    ASC );

ALTER TABLE odontologo ADD CONSTRAINT odontologo_pk PRIMARY KEY ( idodontologo );

CREATE TABLE ordenpedido (
    idpedido NUMBER(10) NOT NULL
);

ALTER TABLE ordenpedido ADD CONSTRAINT ordenpedido_pk PRIMARY KEY ( idpedido );

CREATE TABLE paciente (
    idpaciente         NUMBER(10) NOT NULL,
    rut                VARCHAR2(15 CHAR) NOT NULL,
    idtramoprevision   NUMBER(2) NOT NULL
);

CREATE UNIQUE INDEX paciente__idx ON
    paciente (
        rut
    ASC );


ALTER TABLE paciente ADD CONSTRAINT paciente_pk PRIMARY KEY ( idpaciente );

CREATE TABLE persona (
    rut               VARCHAR2(15 CHAR) NOT NULL,
    nombre            VARCHAR2(50 CHAR),
    apellidopaterno   VARCHAR2(50 CHAR),
    apellidomaterno   VARCHAR2(50 CHAR),
    email             VARCHAR2(100 CHAR),
    genero            VARCHAR2(15),
    telefono          VARCHAR2(15 CHAR),
    fechanac          DATE,
    idtipoper         NUMBER(1) NOT NULL,
    vigente           NUMBER(1)
);

ALTER TABLE persona ADD CONSTRAINT persona_pk PRIMARY KEY ( rut );

CREATE TABLE prevision (
    idprevision    VARCHAR2(1) NOT NULL,
    nomprevision   VARCHAR2(50)
);

ALTER TABLE prevision ADD CONSTRAINT prevision_pk PRIMARY KEY ( idprevision );

CREATE TABLE producto (
    idproducto     NUMBER(10) NOT NULL,
    nomproducto    VARCHAR2(100 CHAR),
    sku            VARCHAR2(100 CHAR),
    marca	   VARCHAR2(100 char),
    descripcion    VARCHAR2(300 CHAR),
    vencimiento    DATE,
    preciocompra   NUMBER(10),
    precioventa    NUMBER(10),
    stock          NUMBER(10),
    stockcritico   NUMBER,
    idproveedor    NUMBER(5) NOT NULL,
    idcategoria     NUMBER(5)
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( idproducto );

CREATE TABLE proveedor (
    idproveedor   NUMBER(5) NOT NULL,
    rut           VARCHAR2(15 CHAR) NOT NULL
);

CREATE UNIQUE INDEX proveedor__idx ON
    proveedor (
        rut
    ASC );

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( idproveedor );

CREATE TABLE reserva (
    idreserva        NUMBER(10) NOT NULL,
    fecha            DATE,
    idpaciente       NUMBER(10) NOT NULL,
    idespecialidad   NUMBER(10) NOT NULL,
    idhora           NUMBER(10) NOT NULL,
    idestado         NUMBER(1) NOT NULL
);

CREATE UNIQUE INDEX reserva__idx ON
    reserva (
        idhora
    ASC );

ALTER TABLE reserva ADD CONSTRAINT reserva_pk PRIMARY KEY ( idreserva );

CREATE TABLE servicio (
    idservicio       NUMBER(5) NOT NULL,
    idtiposervicio   NUMBER(5) NOT NULL,
    nomservicio      VARCHAR2(50 CHAR),
    descripcion      VARCHAR2(100 CHAR),
    valor            NUMBER
);

ALTER TABLE servicio ADD CONSTRAINT servicio_pk PRIMARY KEY ( idservicio );

CREATE TABLE servicio_producto (
    idproducto   NUMBER(10) NOT NULL,
    idservicio   NUMBER(5) NOT NULL
);

ALTER TABLE servicio_producto ADD CONSTRAINT producto_servicio_pk PRIMARY KEY ( idproducto,
                                                                                idservicio );

CREATE TABLE tipoempleado (
    idtipoemp     NUMBER(5) NOT NULL,
    nomtipoemp    VARCHAR2(50 CHAR),
    descripcion   VARCHAR2(100 CHAR)
);

ALTER TABLE tipoempleado ADD CONSTRAINT tipoempleado_pk PRIMARY KEY ( idtipoemp );

CREATE TABLE tipopersona (
    idtipoper     NUMBER(1) NOT NULL,
    nomtipo       VARCHAR2(50 CHAR),
    descripcion   VARCHAR2(100 CHAR)
);

ALTER TABLE tipopersona ADD CONSTRAINT tipopersona_pk PRIMARY KEY ( idtipoper );

CREATE TABLE tiposervicio (
    idtiposervicio   NUMBER(5) NOT NULL,
    nomtipo          VARCHAR2(50 CHAR)
);

ALTER TABLE tiposervicio ADD CONSTRAINT tiposervicio_pk PRIMARY KEY ( idtiposervicio );

CREATE TABLE tramo_prevision (
    idtramoprevision   NUMBER(2) NOT NULL,
    descripcion        VARCHAR2(100),
    costo_pago         FLOAT,
    idprevision        VARCHAR2(1) NOT NULL
);

ALTER TABLE tramo_prevision ADD CONSTRAINT tramo_prevision_pk PRIMARY KEY ( idtramoprevision );

CREATE TABLE usuario (
    idusuario   NUMBER(10) NOT NULL,
    rut         VARCHAR2(15 CHAR) NOT NULL,
    clave       VARCHAR2(200 CHAR),
    admin       NUMBER(1),
    idacceso    NUMBER(2) NOT NULL
);

CREATE UNIQUE INDEX usuario__idx ON
    usuario (
        rut
    ASC );

ALTER TABLE usuario ADD CONSTRAINT usuario_pk PRIMARY KEY ( idusuario );

CREATE TABLE categoria (
idcategoria NUMBER (5) NOT NULL,
nomcategoria VARCHAR2(50 CHAR),
descripcion VARCHAR2(300 CHAR)
);

ALTER TABLE categoria ADD CONSTRAINT categoria_pk PRIMARY KEY ( idcategoria );


ALTER TABLE atencion
    ADD CONSTRAINT atencion_odontologo_fk FOREIGN KEY ( idodontologo )
        REFERENCES odontologo ( idodontologo );

ALTER TABLE atencion
    ADD CONSTRAINT atencion_reserva_fk FOREIGN KEY ( idreserva )
        REFERENCES reserva ( idreserva );

ALTER TABLE boleta
    ADD CONSTRAINT boleta_atencion_fk FOREIGN KEY ( idatencion )
        REFERENCES atencion ( idatencion );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE control_recepcion_pedido_producto
    ADD CONSTRAINT control_recepcion_pedido_producto_estado_recepcion_fk FOREIGN KEY ( idestadorecepcion )
        REFERENCES estado_recepcion ( idestadorecepcion );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE control_recepcion_pedido_producto
    ADD CONSTRAINT control_recepcion_pedido_producto_ordenpedido_fk FOREIGN KEY ( idpedido )
        REFERENCES ordenpedido ( idpedido );

ALTER TABLE detalle_boleta
    ADD CONSTRAINT detalle_boleta_boleta_fk FOREIGN KEY ( idboleta )
        REFERENCES boleta ( idboleta );

ALTER TABLE detalle_boleta
    ADD CONSTRAINT detalle_boleta_servicio_fk FOREIGN KEY ( idservicio )
        REFERENCES servicio ( idservicio );

ALTER TABLE detalle_pedido
    ADD CONSTRAINT detalle_pedido_ordenpedido_fk FOREIGN KEY ( idpedido )
        REFERENCES ordenpedido ( idpedido );

ALTER TABLE detalle_pedido
    ADD CONSTRAINT detalle_pedido_producto_fk FOREIGN KEY ( idproducto )
        REFERENCES producto ( idproducto );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_persona_fk FOREIGN KEY ( rut )
        REFERENCES persona ( rut );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_tipoempleado_fk FOREIGN KEY ( idtipoemp )
        REFERENCES tipoempleado ( idtipoemp );

ALTER TABLE especialidad_odontologo
    ADD CONSTRAINT espe_odontologo_espe_fk FOREIGN KEY ( idespecialidad )
        REFERENCES especialidad ( idespecialidad );

ALTER TABLE especialidad_odontologo
    ADD CONSTRAINT espe_odontologo_odon_fk FOREIGN KEY ( idodontologo )
        REFERENCES odontologo ( idodontologo );

ALTER TABLE estado_pedido
    ADD CONSTRAINT estado_pedido_ordenpedido_fk FOREIGN KEY ( idpedido )
        REFERENCES ordenpedido ( idpedido );

ALTER TABLE odontologo
    ADD CONSTRAINT odontologo_persona_fk FOREIGN KEY ( rut )
        REFERENCES persona ( rut );

ALTER TABLE paciente
    ADD CONSTRAINT paciente_persona_fk FOREIGN KEY ( rut )
        REFERENCES persona ( rut );

ALTER TABLE paciente
    ADD CONSTRAINT paciente_tramo_prevision_fk FOREIGN KEY ( idtramoprevision )
        REFERENCES tramo_prevision ( idtramoprevision );

ALTER TABLE persona
    ADD CONSTRAINT persona_tipopersona_fk FOREIGN KEY ( idtipoper )
        REFERENCES tipopersona ( idtipoper );

ALTER TABLE producto
    ADD CONSTRAINT producto_proveedor_fk FOREIGN KEY ( idproveedor )
        REFERENCES proveedor ( idproveedor );

ALTER TABLE PRODUCTO
ADD CONSTRAINT PRODUCTO_CATEGORIA_FK FOREIGN KEY
(
  IDCATEGORIA 
)
REFERENCES CATEGORIA
(
  IDCATEGORIA 
)
ENABLE;

ALTER TABLE servicio_producto
    ADD CONSTRAINT producto_servicio_producto_fk FOREIGN KEY ( idproducto )
        REFERENCES producto ( idproducto );

ALTER TABLE servicio_producto
    ADD CONSTRAINT producto_servicio_servicio_fk FOREIGN KEY ( idservicio )
        REFERENCES servicio ( idservicio );

ALTER TABLE proveedor
    ADD CONSTRAINT proveedor_persona_fk FOREIGN KEY ( rut )
        REFERENCES persona ( rut );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_especialidad_fk FOREIGN KEY ( idespecialidad )
        REFERENCES especialidad ( idespecialidad );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_estado_reserva_fk FOREIGN KEY ( idestado )
        REFERENCES estado_reserva ( idestado );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_horareserva_fk FOREIGN KEY ( idhora )
        REFERENCES horareserva ( idhora );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_paciente_fk FOREIGN KEY ( idpaciente )
        REFERENCES paciente ( idpaciente );

ALTER TABLE servicio
    ADD CONSTRAINT servicio_tiposervicio_fk FOREIGN KEY ( idtiposervicio )
        REFERENCES tiposervicio ( idtiposervicio );

ALTER TABLE tramo_prevision
    ADD CONSTRAINT tramo_prevision_prevision_fk FOREIGN KEY ( idprevision )
        REFERENCES prevision ( idprevision );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_acceso_fk FOREIGN KEY ( idacceso )
        REFERENCES acceso ( idacceso );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_persona_fk FOREIGN KEY ( rut )
        REFERENCES persona ( rut );
