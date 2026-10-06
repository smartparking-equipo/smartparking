# TRA-001 - Matriz de Trazabilidad de smartparking

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: smartparking
- Versión: 1.2
- Estado: En revisión; pendiente de aprobación e integración de este documento
- Fecha: 06/10/2026
- Responsable: Equipo smartparking
- Responsable del cambio CR-001: Revant11y
- Responsable del cambio CR-001: SaraArias801


## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 04/10/2026 | Creación inicial de la matriz de trazabilidad | Equipo smartparking |
| 1.1 | 05/10/2026 | Actualización de la trazabilidad asociada a CR-001 - Agregar atributo espacio asignado  | Revant11y |
| 1.2 | 06/10/2026 | Se relaciona CR-002 con requisitos, diseño, código y pruebas sobre necesidad de carga y espacios con cargador. | SaraArias801 |

**Antecedente documental:** el 06/10/2026 se registró la aprobación de TRA-001 v1.1 para CR-001, según la actualización atribuida a SaraArias801. Esta entrada conserva el historial anterior; no constituye una aprobación de la presente versión 1.2.



## 1. Objetivo

Relacionar los requisitos de SmartParking con el diseño, el código fuente y las pruebas que los implementan o verifican. La versión 1.2 agrega la trazabilidad de CR-002 sin borrar la correspondiente al producto inicial y a CR-001.

## 2. Matriz de trazabilidad inicial

Las primeras seis filas conservan las referencias registradas en TRA-001 v1.1. En las filas nuevas se deben sustituir los campos entre corchetes por los identificadores y versiones que consten en los CI modificados por el equipo. 

| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
|-----------|-------------|--------------------|--------------------|--------------------|--------|
| RF-001 | Registro de vehículo | DES-001 v1.1 - Diseño del Sistema | SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1  / CP-001, CP-002 | Completa |
| RF-002 | Registro de ingreso | DES-001 v1.1 - Diseño del Sistema | SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-003, CP-004 | Completa |
| RF-003 | Registro de salida de vehículos | DES-001 v1.1 - Diseño del Sistema| SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-006,  | Completa |
| RF-004 | Consulta de Disponibilidad | DES-001 v1.1 - Diseño del Sistema| SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-008, CP-009 | Completado |
| RF-005 | Cálculo del tiempo de permanencia | DES-001 v1.1 - Diseño del Sistema | SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-010 | Completado |
| RF-006 | Consulta de información del vehículo | DES-001 v1.1 - Diseño del Sistema | SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-011, CP-012 | Completado |
| RF-007 | CR-002: registrar y consultar si un vehículo requiere carga. | DES-001 v1.2 — Atributo del vehículo y flujo de consulta. | SRC-001 v1.2 | TST-001 v1.2. | Completado |
| RF-008 | CR-002: identificar y consultar qué espacios cuentan con cargador. | DES-001 v1.2 — Atributo del espacio y consulta. | SRC-001 v1.2 | TST-001 v1.2 /  | Completado |

**Alcance aprobado de CR-002:** identificar los vehículos que requieren carga y los espacios con cargador. No atribuir a CR-002 una nueva regla de asignación automática a menos que esa regla también figure explícitamente aprobada en la solicitud y sus CI asociados.

## 3. Relación entre elementos de configuración

La trazabilidad de CR-002 sigue esta relación:

```text
CR-002 — Solicitud aprobada
  ↓
ESP-001 [versión real] — Requisitos de vehículo y espacio
  ↓
DES-001 [versión real] — Diseño de los datos y consultas
  ↓
SRC-001 [versión real] — Implementación
  ↓
TST-001 [versión real] — Casos y resultados de prueba
  ↓
PR de implementación 
```

TRA-001 v1.2 registra estas relaciones. Las versiones se toman de cada CI y no se infieren únicamente de la versión del producto.

## 4. Trazabilidad por requisito

### RF-01 - Registrar Vehículo

- Requisito: ESP-001 v1.1
- Diseño asociado: DES-001 v1.1 - Entidad Vehículo
- Código asociado: SRC-001 v1.1 - Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 v1.1 / CP-001, CP-002
- Estado de trazabilidad: Completa

### RF-02 - Registro de ingreso

- Requisito: ESP-001 v1.1
- Diseño asociado: DES-001 v1.1 - Entidad Vehículo
- Código asociado: SRC-001 v1.1 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 v1.1 / CP-003, CP-004
- Estado de trazabilidad: Completa

### RF-03 - Registro de salida de vehículos

- Requisito: ESP-001 v1.1
- Diseño asociado: DES-001 v1.1 - Entidad Vehículo
- Código asociado: SRC-001 v1.1 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 v1.1 / CP-006
- Estado de trazabilidad: Completa

### RF-04 - Consulta de disponibilidad

- Requisito: ESP-001 v1.1
- Diseño asociado: DES-001 v1.1  - Entidad Vehículo
- Código asociado: SRC-001 v1.1 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 v1.1 / CP-008,  CP-009
- Estado de trazabilidad: Completo

### RF-05 - Cálculo del tiempo de permanencia
- Requisito: ESP-001 v1.1
- Diseño asociado: DES-001 v1.1 - Entidad Vehículo
- Código asociado: SRC-001 v1.1 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 v1.1 / CP-010
- Estado de trazabilidad: Completo

### RF-06 - Consulta de información del vehículo

- Requisito: ESP-001 v1.1
- Diseño asociado: DES-001 v1.1 - Entidad Vehículo
- Código asociado: SRC-001 v1.1 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 v1.1 / CP-011, CP-012
- Estado de trazabilidad: Completo

### RF-07 Identificación de vehículos que requieren carga

- Solicitud: CR-002, aprobada.
- Requisito: ESP-001 v1.2 
- Diseño asociado: DES-001 v1.2
- Código asociado: SRC-001 v1.2
- Prueba asociada: TST-001 v1.2 


### RF-08 Identificación de espacios con cargador

- Solicitud: CR-002, aprobada.
- Requisito: ESP-001 v1.2 
- Diseño asociado: DES-001 v1.2
- Código asociado: SRC-001 v1.2
- Prueba asociada: TST-001 v1.2 

## 5. Trazabilidad de cambios

Cuando se apruebe una solicitud de cambio, esta matriz deberá registrar qué elementos fueron afectados.

La relación deberá seguir, cuando aplique, la siguiente estructura:

Solicitud de cambio
↓
Requisito afectado
↓
Diseño afectado
↓
Código afectado
↓
Prueba afectada
↓
Commit o Pull Request
↓
Nueva versión de los elementos afectados

## 6. Registro de cambios trazables

| Solicitud de cambio | Requisito afectado | Diseño afectado | Código afectado | Prueba afectada | Commit / PR | Estado |
|--------------------|--------------------|-----------------|-----------------|-----------------|-------------|--------|
| Sin cambios aprobados en la versión 1.0 | - | - | - | - | - | Línea base inicial |
| CR-001 - Agregar atributo espacio asignación | ESP-001 v1.1 / RF-01 | DES-001 v1.1 | SRC-001 v1.1 | TST-001 v1.1 / CP-01 | PR #2 | Aprobado |
| CR-002 — Vehículos que requieren carga | ESP-001 v1.2 / RF-07 | DES-001 v1.2 | SRC-001 v1.2 | TST-001 v1.2 | PR #5 | Aprobado |
| CR-002 — Espacios con cargador | ESP-001 v1.2 / RF-08 | DES-001 v1.2 | SRC-001 v1.2 | TST-001 v1.2 | PR #5 | Aprobado |

## 7. Observaciones

TRA-001 v1.2 conserva el historial de la versión 1.1 e incorpora las relaciones de CR-002. Los campos entre corchetes no son referencias aprobadas: se deben completar con los cambios y pruebas reales del equipo antes de solicitar la aprobación de este documento.

La matriz anterior de CR-001 todavía indicaba «PR #2 / Pendiente por revisión» pese a que después se integró la solicitud. En esta versión se actualiza el estado histórico a integrado y se deja señalado que el número de PR y los casos de prueba deben verificarse. También se corrige la relación principal de la asignación de espacio hacia el requisito de ingreso RF-002; el vínculo con disponibilidad RF-004 se confirmará en ESP-001.

Después de aprobar e integrar TRA-001 v1.2 junto con los demás CI de CR-002, se podrá preparar la siguiente línea base. La etiqueta `v1.2` debe señalar el commit de `main` que incluya la documentación aprobada.
