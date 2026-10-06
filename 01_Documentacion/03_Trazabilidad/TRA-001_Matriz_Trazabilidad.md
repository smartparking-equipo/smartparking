# TRA-001 - Matriz de Trazabilidad de smartparking

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: smartparking
- Versión: 1.0
- Fecha: 10/04/2026
- Responsable: Equipo smartparking


## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 04/10/2026 | Creación inicial de la matriz de trazabilidad | Equipo smartparking |


## 1. Objetivo

Relacionar los requisitos definidos para smartparking con los elementos de diseño, código fuente y pruebas que los implementan o verifican.

La matriz permite identificar qué elementos de configuración deben revisarse cuando un requisito sea modificado.

## 2. Matriz de trazabilidad inicial

| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
|-----------|-------------|--------------------|--------------------|--------------------|--------|
| RF-001 | Registro de vehículo | DES-001 - Diseño del Sistema | SRC-001 - Gestión de Parqueadero Core | TST-001  / CP-001, CP-002 | Completa |
| RF-002 | Registro de ingreso | DES-001 - Diseño del Sistema | SRC-001 - Gestión de Parqueadero Core | TST-001 / CP-003, CP-004 | Completa |
| RF-003 | Registro de salida de vehículos | DES-001 - Diseño del Sistema| SRC-001 - Gestión de Parqueadero Core | TST-001 / CP-006,  | Completa |
| RF-004 | Consulta de Disponibilidad | DES-001 - Diseño del Sistema| SRC-001 - Gestión de Parqueadero Core | TST-001 / CP-008, CP-009 | Completado |
| RF-005 | Cálculo del tiempo de permanencia | DES-001 - Diseño del Sistema | SRC-001 - Gestión de Parqueadero Core | TST-001 / CP-010 | Parcial |
| RF-006 | Consulta de información del vehículo | DES-001 - Diseño del Sistema | SRC-001 - Gestión de Parqueadero Core | TST-001 / CP-011, CP-012 | Parcial |


## 3. Relación entre elementos de configuración

La configuración inicial de smartparking presenta la siguiente relación:

ESP-001 v1.0
↓
DES-001 v1.0
↓
SRC-001 v1.0
↓
TST-001 v1.0

El elemento TRA-001 registra y documenta estas relaciones.

## 4. Trazabilidad por requisito

### RF-01 - Registrar Vehículo

- Requisito: ESP-001
- Diseño asociado: DES-001 - Entidad Vehículo
- Código asociado: SRC-001 - Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 / CP-001, CP-002
- Estado de trazabilidad: Completa

### RF-02 - Registro de ingreso

- Requisito: ESP-001
- Diseño asociado: DES-001 - Entidad Vehículo
- Código asociado: SRC-001 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 / CP-003, CP-004
- Estado de trazabilidad: Completa

### RF-03 - Registro de salida de vehículos

- Requisito: ESP-001
- Diseño asociado: DES-001 - Entidad Vehículo
- Código asociado: SRC-001 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 / CP-006
- Estado de trazabilidad: Completa

### RF-04 - Consulta de disponibilidad

- Requisito: ESP-001
- Diseño asociado: DES-001 - Entidad Vehículo
- Código asociado: SRC-001 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 / CP-008,  CP-009
- Estado de trazabilidad: Parcial

### RF-05 - Cálculo del tiempo de permanencia

- Requisito: ESP-001
- Diseño asociado: DES-001 - Entidad Vehículo
- Código asociado: SRC-001 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 / CP-010
- Estado de trazabilidad: Parcial

### RF-06 - Consulta de información del vehículo

- Requisito: ESP-001
- Diseño asociado: DES-001 - Entidad Vehículo
- Código asociado: SRC-001 -  Gestión de Parqueadero Core
- Caso de prueba asociado: TST-001 / CP-011, CP-012
- Estado de trazabilidad: Parcial



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

## 7. Observaciones

Este documento constituye el Elemento de Configuración TRA-001.

La versión 1.0 representa la trazabilidad correspondiente a la configuración inicial de smartparking .

Toda modificación posterior deberá actualizar esta matriz y quedar relacionada con una solicitud de cambio aprobada.