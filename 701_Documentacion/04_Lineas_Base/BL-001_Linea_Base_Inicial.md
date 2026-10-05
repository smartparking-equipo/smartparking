# BL-001 - Línea Base Inicial de SmartParking

## Información de la línea base

- Código: BL-001
- Proyecto: SmartParking
- - Nombre: Línea Base Inicial
- Versión del producto: 1.0
- Fecha de establecimiento: 04/10/2026
- - Estado: Aprobada
- Responsable: Equipo SmartParking

## 1. Objetivo
Gestión de parqueadero. SmartParking controla el ingreso y salida de vehículos de un parqueadero universitario. 

## 2. Elementos incluidos en la línea base

| Código CI | Elemento de configuración | Versión | Estado |
|-----------|---------------------------|---------|--------|
| ESP-001 | Especificación de Requisitos | 1.0 | Aprobado |
| DES-001 | Diseño del Sistema | 1.0 | Aprobado |
| SRC-001 | Gestión de Estudiantes | 1.0 | Aprobado |
| TST-001 | Plan y Casos de Prueba | 1.0 | Aprobado |
| TRA-001 | Matriz de Trazabilidad | 1.0 | Aprobado |


## 3. Relaciones de trazabilidad

La configuración aprobada mantiene la siguiente relación:

ESP-001 v1.0
↓
DES-001 v1.0
↓
SRC-001 v1.0
↓
TST-001 v1.0

TRA-001 v1.0 documenta las relaciones existentes entre estos elementos.

## 4. Criterio de establecimiento

La línea base BL-001 se establece debido a que:

- Los requisitos iniciales han sido definidos.
- El diseño correspondiente ha sido documentado.
- Existe una implementación inicial del módulo de estudiantes.
- Se han definido los casos de prueba relacionados.
- Se ha establecido la trazabilidad entre los elementos de configuración.

## 5. Control posterior de cambios

Una vez establecida BL-001, los elementos incluidos no deberán modificarse directamente sin identificar y documentar el cambio.

Todo cambio posterior deberá:

1. Originarse en una solicitud de cambio.
2. Identificar los CI afectados.
3. Analizar su impacto.
4. Realizarse en una rama de trabajo.
5. Quedar registrado mediante commits.
6. Ser revisado antes de integrarse a la rama principal.
7. Actualizar la trazabilidad correspondiente.
8. Generar, cuando corresponda, una nueva versión y una nueva línea base.

## 6. Identificación técnica

La línea base BL-001 será identificada en el repositorio Git mediante la etiqueta:

`v1.0`

Esta etiqueta permitirá recuperar posteriormente el estado exacto del repositorio correspondiente a esta línea base.

## 7. Observaciones

BL-001 representa la configuración aprobada inicial de SmartParking.

Las futuras modificaciones no alterarán esta línea base. En caso de aprobarse cambios, se establecerá una nueva configuración y posteriormente una nueva línea base.
