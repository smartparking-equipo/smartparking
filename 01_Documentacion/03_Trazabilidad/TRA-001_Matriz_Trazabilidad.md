# TRA-001 - Matriz de Trazabilidad de smartparking

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: smartparking
- Versión: 1.3
- Estado: Aprobado para BL-002; CR-002 implementada y cerrada
- Fecha: 06/10/2026
- Fecha de cierre: 07/10/2026
- Responsable: Equipo smartparking
- Responsable del cambio CR-001: Revant11y
- Responsable del cambio CR-001: SaraArias801
- Responsable del cambio CR-002: alexagr210

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 04/10/2026 | Creación inicial de la matriz de trazabilidad | Equipo smartparking |
| 1.1 | 05/10/2026 | Actualización de la trazabilidad asociada a CR-001 - Agregar atributo espacio asignado  | Revant11y |
| 1.2 | 06/10/2026 | Se relaciona CR-002 con requisitos, diseño, código y pruebas sobre necesidad de carga y espacios con cargador. | alexagr210 |

**Antecedente documental:** el 06/10/2026 se registró la aprobación de TRA-001 v1.1 para CR-001, según la actualización atribuida a SaraArias801. Esta entrada conserva el historial anterior; no constituye una aprobación de la presente versión 1.2.

## 1. Objetivo

Relacionar los requisitos de SmartParking con el diseño, el código fuente y las pruebas que los implementan o verifican. La versión 1.2 agrega la trazabilidad de CR-002 sin borrar la correspondiente al producto inicial y a CR-001.

## 2. Matriz de trazabilidad inicial

Las primeras seis filas conservan las referencias registradas en TRA-001 v1.1. En las filas nuevas se han sustituido los campos abiertos de acuerdo con las versiones y códigos reales vigentes en los CI modificados por el equipo para dar cumplimiento a CR-002.

| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
|-----------|-------------|--------------------|--------------------|--------------------|--------|
| RF-001 | Registro de vehículo | DES-001 v1.1 - Diseño del Sistema | SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1  / CP-001, CP-002 | Completa |
| RF-002 | Registro de ingreso | DES-001 v1.1 - Diseño del Sistema | SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-003, CP-004 | Completa |
| RF-003 | Registro de salida de vehículos | DES-001 v1.1 - Diseño del Sistema| SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-006 | Completa |
| RF-004 | Consulta de Disponibilidad | DES-001 v1.1 - Diseño del Sistema| SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-008, CP-009 | Completado |
| RF-005 | Cálculo del tiempo de permanencia | DES-001 v1.1 - Diseño del Sistema | SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-010 | Completado |
| RF-006 | Consulta de información del vehículo | DES-001 v1.1 - Diseño del Sistema | SRC-001 v1.1 - Gestión de Parqueadero Core | TST-001 v1.1 / CP-011, CP-012 | Completado |
| RF-007 | CR-002: registrar y consultar si un vehículo requiere carga. | DES-001 v1.2 — Sección 4.2 Entidad Vehículo (atributo tipo_vehiculo) | SRC-001 v1.2 — Clase Vehículo y función registrar_ingreso() | TST-001 v1.2 / CP-015, CP-017, CP-020 | Completado |
| RF-008 | CR-002: identificar y consultar qué espacios cuentan con cargador. | DES-001 v1.2 — Sección 4.2 Entidad Celda (atributo tiene_cargador) | SRC-001 v1.2 — Clase Celda y función consultar_disponibilidad() | TST-001 v1.2 / CP-016, CP-021 | Completado |

**Alcance aprobado de CR-002:** identificar los vehículos que requieren carga y los espacios con cargador. Se incorporan las reglas de asignación por prioridad energética y contingencia (RN-005) para asegurar el correcto direccionamiento e integridad operativa del sistema de control.

## 3. Relación entre elementos de configuración

La trazabilidad de CR-002 sigue esta relación:

```text
CR-002 — Solicitud aprobada
  ↓
ESP-001 v1.2 — Requisitos de vehículo (RF-001/RF-006/RF-007) y espacio (RF-002/RF-004/RF-008)
  ↓
DES-001 v1.2 — Diseño de entidades (Vehículo, Celda), diccionario de datos y flujo operacional 6.2
  ↓
SRC-001 v1.2 — Implementación de clases Vehiculo/Celda y algoritmo privado _buscar_espacio_disponible()
  ↓
TST-001 v1.2 — Casos de prueba funcionales desde CP-015 hasta CP-021
  ↓
PR #5 de implementación y cierre documental unificado
  ↓
PR #6 aprobado y fusionado
```

TRA-001 v1.2 registra estas relaciones. Las versiones se toman de cada CI y no se infieren únicamente de la versión del producto.

## 4. Trazabilidad por requisito

### RF-001 - Registro de vehículo

- Requisito: ESP-001 v1.2
- Diseño asociado: DES-001 v1.2 - Entidad Vehículo (atributo tipo_vehiculo)
- Código asociado: SRC-001 v1.2 - Clase Vehiculo y clase SmartParking
- Caso de prueba asociado: TST-001 v1.2 / CP-001, CP-002, CP-015
- Estado de trazabilidad: Completa

### RF-002 - Registro de ingreso

- Requisito: ESP-001 v1.2
- Diseño asociado: DES-001 v1.2 - Flujo de Operación 6.2 y Regla RN-005
- Código asociado: SRC-001 v1.2 - función registrar_ingreso() y algoritmo _buscar_espacio_disponible()
- Caso de prueba asociado: TST-001 v1.2 / CP-003, CP-004, CP-017, CP-018, CP-019, CP-020
- Estado de trazabilidad: Completa

### RF-003 - Registro de salida de vehículos

- Requisito: ESP-001 v1.2
- Diseño asociado: DES-001 v1.2 - Flujo de Operación 6.3 y mutación de la Entidad Celda
- Código asociado: SRC-001 v1.2 - función registrar_salida()
- Caso de prueba asociado: TST-001 v1.2 / CP-006, CP-007
- Estado de trazabilidad: Completa

### RF-004 - Consulta de disponibilidad

- Requisito: ESP-001 v1.2
- Diseño asociado: DES-001 v1.2 - Sección 5 (Fórmula de Disponibilidad Desglosada) y Operación 6.4
- Código asociado: SRC-001 v1.2 - función consultar_disponibilidad()
- Caso de prueba asociado: TST-001 v1.2 / CP-008, CP-009, CP-021
- Estado de trazabilidad: Completo

### RF-005 - Cálculo del tiempo de permanencia

- Requisito: ESP-001 v1.2
- Diseño asociado: DES-001 v1.2 - Operación 6.5 e instantes de Entancia
- Código asociado: SRC-001 v1.2 - función calcular_tiempo_permanencia() en el método de salida
- Caso de prueba asociado: TST-001 v1.2 / CP-010
- Estado de trazabilidad: Completo

### RF-006 - Consulta de información del vehículo

- Requisito: ESP-001 v1.2
- Diseño asociado: DES-001 v1.2 - Operación 6.6 y derivación de estado Dentro/Fuera
- Código asociado: SRC-001 v1.2 - mapa de diccionario vehiculos_activos y consulta por placa
- Caso de prueba asociado: TST-001 v1.2 / CP-011, CP-012
- Estado de trazabilidad: Completo

### RF-007 - Identificación de vehículos que requieren carga [CR-002]

- Solicitud: CR-002, aprobada.
- Requisito: ESP-001 v1.2 - Requisito Funcional RF-001 y Regla de Negocio RN-005
- Diseño asociado: DES-001 v1.2 - Diccionario de Datos (Vehículo -> atributo tipo_vehiculo)
- Código asociado: SRC-001 v1.2 - Clase Vehiculo (inicialización del tipo de motorización)
- Prueba asociada: TST-001 v1.2 / CP-015, CP-017, CP-020
- Estado de trazabilidad: Completa

### RF-008 - Identificación de espacios con cargador [CR-002]

- Solicitud: CR-002, aprobada.
- Requisito: ESP-001 v1.2 - Requisito Funcional RF-007 y Consulta RF-004
- Diseño asociado: DES-001 v1.2 - Diccionario de Datos (Celda -> atributo tiene_cargador)
- Código asociado: SRC-001 v1.2 - Clase Celda (parámetro de infraestructura de carga)
- Prueba asociada: TST-001 v1.2 / CP-016, CP-021
- Estado de trazabilidad: Completa

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
| CR-001 - Agregar atributo espacio asignación | ESP-001 v1.1 / RF-002 | DES-001 v1.1 | SRC-001 v1.1 | TST-001 v1.1 / CP-003 | PR #2 | Aprobado |
| CR-002 — Vehículos que requieren carga | ESP-001 v1.2 / RF-001, RF-007 | DES-001 v1.2 | SRC-001 v1.2 | TST-001 v1.2 / CP-015, CP-017 | PR #5 | Aprobado |
| CR-002 — Espacios con cargador | ESP-001 v1.2 / RF-007, RF-004 | DES-001 v1.2 | SRC-001 v1.2 | TST-001 v1.2 / CP-016, CP-021 | PR #6 | Aprobado|


## 7. Observations

TRA-001 v1.2 conserva el historial de la versión 1.1 e incorpora las relaciones de CR-002. Los campos abiertos han sido completados con las trazas y referencias reales a los CIs desarrollados por el equipo, eliminando ambigüedades antes de solicitar la aprobación final.

La matriz anterior de CR-001 todavía indicaba «PR #2 / Pendiente por revisión» pese a que después se integró la solicitud. En esta versión se actualiza el estado histórico a integrado y se deja señalado que el número de PR y los casos de prueba han sido verificados. También se corrige la relación principal de la asignación de espacio hacia el requisito de ingreso RF-002; el vínculo con disponibilidad RF-004 se encuentra confirmado en ESP-001 v1.2.

Después de aprobar e integrar TRA-001 v1.2 junto con los demás CI de CR-002, se podrá preparar la siguiente línea base. La etiqueta `v1.2` debe señalar el commit de `main` que incluya la documentación aprobada.
