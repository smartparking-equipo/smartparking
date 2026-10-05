# ESP-001 - Especificacion de Requisitos

## . Informacion del elemento de configuracion

| Campo | Informacion |
|---|---|
| Codigo | ESP-001 |
| Nombre | Especificacion de Requisitos SmartParking |
| Version | 1.1 |
| Estado | En modificacion CR-001|
| Fecha | 2026-10-04  |
| Sistema | SmartParking - Gestion de Parqueadero |
| Responsable del cambio| Santiago1054 |

RFE-01: Asignación de espacio
Control de versiones

| Versión | Fecha | Descripción | Responsable |
|---|---|---|---|
| 1.0 | 2026-10-04 | Creación de la especificación inicial | Equipo SmartParking |
| 1.1 | 2026-10-04 | Creación de la Asignación de espacio | Equipo SmartParking |

## 1. Proposito

SmartParking es un sistema para gestionar el ingreso y salida de
vehiculos de un parqueadero universitario El sistema permite llevar
el control de los vehiculos que ingresan registrar su salida 
consultar la disponibilidad de espacios y calcular el tiempo de
permanencia



## 2. Alcance inicial

La version inicial del sistema contempla las siguientes funciones:

- Registrar vehiculos.
- Registrar el ingreso de vehiculos.
- Registrar la salida de vehiculos.
- Consultar los espacios disponibles.
- Calcular el tiempo de permanencia de un vehículo.


## 3. Requisitos funcionales

### RF-001 – Registro de vehículo
El sistema debe permitir registrar un vehículo ingresando como mínimo los siguientes datos:
- Placa
- Marca
- Color

Criterio de aceptación:

El sistema debe almacenar correctamente la información del vehículo cuando todos los datos obligatorios hayan sido suministrados.

### RF-002 – Registro de ingreso
El sistema debe permitir registrar el ingreso de un vehículo, almacenando los siguientes datos:
- Placa del vehículo
- Fecha de entrada
- Hora de entrada
- Espacio de asignación 

Criterio de aceptacion:
El vehiculo tiene que estar previamente registrado para el registro de ingreso.

### RF-003 - Registro de salida de vehículos

El sistema deberá permitir registrar la salida de un vehículo que se encuentre dentro del parqueadero, almacenando la placa del vehículo, la fecha y la hora exacta de salida. y liberando el espacio de asignación.

### RF-004 - Consulta de disponibilidad

El sistema deberá permitir consultar la cantidad de espacios disponibles en el parqueadero, teniendo en cuenta los vehículos que se encuentren actualmente dentro de las instalaciones.

### RF-005 - Cálculo del tiempo de permanencia

El sistema deberá calcular el tiempo total de permanencia de un vehículo dentro del parqueadero, utilizando como referencia la fecha y hora de ingreso y la fecha y hora de salida.

### RF-006 - Consulta de información del vehículo

El sistema deberá permitir consultar la información de un vehículo mediante su placa, mostrando sus datos básicos de identificación y su estado actual dentro del parqueadero.


---

## 4. Requisitos no funcionales

### RNF-001 - Usabilidad

El sistema debe presentar las operaciones principales de manera
clara para facilitar su utilización.

### RNF-002 - Integridad de la información

El sistema debe conservar correctamente los datos relacionados
con los vehículos, ingresos y salidas registrados.

### RNF-003 - Trazabilidad

Los cambios realizados sobre los requisitos y demás elementos de
configuración deben poder relacionarse con las solicitudes de
cambio correspondientes.

### RNF-004 - Mantenibilidad

El código y la documentación deben mantenerse organizados para
facilitar futuras modificaciones.

---

## 5. Reglas de negocio

### RN-001

Un vehículo debe estar registrado antes de realizar un ingreso.

### RN-002

Un vehículo que se encuentre registrado como ingresado no debe
registrar un nuevo ingreso hasta completar su salida.

### RN-003

La disponibilidad del parqueadero debe reflejar los espacios
ocupados y liberados por los vehículos.

### RN-004

El tiempo de permanencia se obtiene a partir de la diferencia
entre la hora de salida y la hora de ingreso.

---

## 6. Restricciones de la versión 1.0

La versión inicial no contempla:

- Asignación automática de espacios.
- Gestión de vehículos eléctricos.
- Gestión de espacios con cargadores.
- Reservas permanentes de espacios.

Estas funcionalidades serán tratadas posteriormente mediante
solicitudes de cambio.

---

## 7. Criterios de aceptación

La versión 1.0 se considera funcional cuando:

1. Es posible registrar un vehículo.
2. Es posible registrar su ingreso.
3. Es posible registrar su salida.
4. Es posible consultar los espacios disponibles.
5. Es posible calcular el tiempo de permanencia.
6. Las operaciones anteriores funcionan de manera coherente entre sí.
7. Es posible asignar un espacio a cada vehículo que ingrese.

---

