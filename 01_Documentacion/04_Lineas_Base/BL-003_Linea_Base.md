# BL-003 - Línea Base 1.2 de SmartParking

## Información de la línea base

- Código: BL-002
- Proyecto: SmartParking
- Nombre: Línea Base de Asignación Automática de Espacio
- Versión del producto: 1.2
- Fecha de establecimiento: 07/10/2026
- Estado: Aprobado
- Responsable: albeirosr
- Línea base anterior: BL-002, identificada con la etiqueta `v1.1`
- Solicitud de cambio incorporada: CR-002 — Identificación de vehículos que requieren carga y espacios con cargador (aprobada)

## 1. Objetivo

Establecer la configuración del producto SmartParking después de incorporar CR-002. SmartParking gestiona el registro de vehículos, el ingreso y la salida de un parqueadero universitario y la consulta de espacios disponibles. En la versión 1.1, al registrar un ingreso, el sistema asigna y registra automáticamente un espacio disponible.En la versión 1.2,Vehículos eléctricos y celdas con cargador

## 2. Elementos incluidos en la línea base

| Código CI | Elemento de configuración | Versión en BL-002 | Estado |
|-----------|---------------------------|-------------------|--------|
| ESP-001 | Especificación de Requisitos | 1.2 | Aprobado; |
| DES-001 | Diseño del Sistema | 1.2 | Aprobado;  |
| SRC-001 | Código fuente de gestión del parqueadero y asignación de espacio | 1.2 | Aprobado;  |
| TST-001 | Plan y Casos de Prueba | 1.2 | Aprobado; |
| TRA-001 | Matriz de Trazabilidad | 1.2 | Aprobado;  |


## 3. Relaciones de trazabilidad

La configuración aprobada de CR-002 debe conservar esta relación:

```text
CR-002 — Identificación de vehículos que requieren carga y espacios con cargador cambio-solicitado
   ↓
ESP-001 v1.2 — Requisito de ingreso y asignación
   ↓
DES-001 v1.2 — Diseño de la asignación
   ↓
SRC-001 v1.2 — Implementación
   ↓
TST-001 v1.2 — Pruebas y resultado
```

TRA-001 v1.2 documenta la relación entre la solicitud de cambio y los elementos de configuración anteriores.

## 4. Criterio de establecimiento

La línea base BL-003 podrá establecerse cuando se confirme que:

1. CR-002 fue aprobada y su análisis de impacto identificó los CI afectados.
2. La especificación, el diseño, el código fuente y la trazabilidad relacionados con CR-002 quedaron integrados en `main`. La captura del historial muestra la integración del pull request **#6**; agregar su enlace como evidencia.
3. La asignación automática de un espacio disponible y la actualización de la disponibilidad se comprobaron con pruebas cuyos resultados quedaron registrados.
4. Los identificadores y versiones de la tabla anterior coinciden con el inventario real de CI y con el contenido integrado.
5. Este documento fue revisado e integrado a `main` mediante su propio pull request.


## 5. Control posterior de cambios

Una vez establecida BL-002, los elementos incluidos no deberán modificarse directamente sin identificar y documentar el cambio. Todo cambio posterior deberá:

1. Originarse en una solicitud de cambio.
2. Identificar los CI afectados y analizar su impacto.
3. Realizarse en una rama de trabajo y registrarse mediante commits.
4. Ser revisado y aprobado antes de integrarse en `main`.
5. Actualizar las pruebas y la trazabilidad correspondientes.
6. Generar, cuando corresponda, nuevas versiones de los CI y otra línea base.

## 6. Identificación técnica

Una vez aprobado e integrado este documento en `main`, la línea base BL-003 se identificará mediante la `v1.2`, creada sobre el commit de `main` que incluya tanto CR-002 como este documento. Esta etiqueta permitirá recuperar el estado exacto del repositorio correspondiente a la línea base.

- Etiqueta: `v1.2`.
- Commit al que apunta la etiqueta: .

## 7. Observaciones

BL-003 incorpora el cambio aprobado CR-002 respecto de BL-002 sin modificar la etiqueta histórica `v1.1`. Los campos marcados para verificación deben resolverse con el repositorio y las evidencias del equipo antes de aprobar la línea base. La creación de este archivo en una rama de documentación aún no establece la línea base: la aprobación, la integración y la etiqueta completan el proceso.
