# TST-001 - Plan y Casos de Prueba

## 1. Información del elemento de configuración

| Campo | Información |
|---|---|
| Código | TST-001 |
| Nombre | Plan y casos de prueba |
| Categoría | Pruebas |
| Versión | 1.2 |
| Estado | En modificacion CR-002 |
| Sistema | SmartParking - Gestión de Parqueadero |
| Especificación que verifica | ESP-001 v1.2 |
| Código que verifica | SRC-001 v1.2 |
| Fecha | 2026/10/06 |
| Responsable del cambio | Victorcano19 |


## Control de versiones

| Versión | Fecha | Descripción | Responsable |
|---|---|---|---|
| 1.0 | 2026-10-04 | Creación del plan y los casos de prueba iniciales | Equipo de SmartParking |
| 1.1 | 2026-10-04 | Se aplican casos de prueba según CR-001 | Equipo de SmartParking |
| 1.2 | 2026-10-06 | Integración de casos de prueba para vehículos eléctricos y espacios con cargador (CR-002) | alexagr210 |

Nota de actualización documental — 06/10/2026: se actualiza el estado del documento a En modificación, conforme a la solicitud de cambio CR-002 (Vehículos eléctricos y celdas con cargador). Se diseñan y añaden nuevos escenarios de prueba funcionales para verificar las reglas de asignación por motorización, el desglose de disponibilidad y la parametrización de cargadores. Responsable de la actualización: alexagr210.

## 2. Propósito

Verificar que la versión 1.2 de SmartParking cumple los requisitos y reglas de negocio de ESP-001 v1.2, de modo que la línea base evolutiva sea coherente entre su especificación, su diseño, su código y su manual.

## 3. Alcance

**Se prueba:** RF-001 a RF-007 y RNF-001 a RNF-004.

## 4. Estrategia

| Aspecto | Definición |
|---|---|
| Tipo de prueba | Funcional, de caja negra, sobre las operaciones del sistema |
| Método | Verificación manual: recorrido del código de SRC-001 y revisión de los documentos contra cada caso |
| Ejecutor | Responsable de pruebas, con apoyo de un segundo integrante |
| Entorno | El definido para la verificación (el sistema debe tener configurada una capacidad parametrizada de N celdas comunes y M celdas eléctricas) |

## 5. Criterios

**Entrada:** los CI de la línea base están completos (ESP-001 v1.2, DES-001 v1.2, SRC-001 v1.2).

**Aceptación:** todos los casos obligatorios se verifican con estado *Aprobado*. Si algún caso falla, se corrige el CI afectado y se repiten las pruebas antes de marcar la línea base.

## 6. Casos de prueba

| ID | Caso | Precondición | Pasos / Entrada | Resultado esperado | Requisito / Regla |
|---|---|---|---|---|---|
| CP-001 | Registrar vehículo con datos completos | Placa no registrada | Registrar placa, marca, color y marcar tipo como "Convencional" | El vehículo queda almacenado con sus datos básicos | RF-001 |
| CP-002 | Registrar vehículo sin un dato obligatorio | Ninguna | Registrar dejando la placa vacía | El sistema no almacena el vehículo e informa el dato faltante | RF-001 |
| CP-003 | Ingreso de vehículo registrado | Vehículo registrado y fuera del parqueadero | Registrar el ingreso con su placa | Se almacena placa, fecha y hora de entrada en la celda asignada automáticamente | RF-002, RN-001 |
| CP-004 | Ingreso de vehículo no registrado | Placa no registrada | Registrar ingreso con esa placa | El ingreso se rechaza con un mensaje | RF-002, RN-001 |
| CP-005 | Segundo ingreso sin haber salido | Vehículo con ingreso activo | Registrar otro ingreso con la misma placa | El ingreso se rechaza | RN-002 |
| CP-006 | Salida de vehículo con ingreso activo | Vehículo con ingreso activo | Registrar la salida con su placa | Se almacena placa, fecha y hora de salida; la celda física se libera | RF-003, RN-003 |
| CP-007 | Reingreso tras completar la salida | Vehículo que ya registró su salida | Registrar un nuevo ingreso | El ingreso se acepta | RN-002 |
| CP-008 | Disponibilidad tras un ingreso | Disponibilidad inicial conocida (D) | Registrar un ingreso y consultar | La disponibilidad global disminuye en uno | RF-004, RN-003 |
| CP-009 | Disponibilidad tras una salida | Vehículo con ingreso activo | Registrar la salida y consultar | La disponibilidad global aumenta en uno | RF-004, RN-003 |
| CP-010 | Cálculo del tiempo de permanencia | Ingreso 08:00 y salida 09:35 del mismo día | Consultar el tiempo de permanencia | 1 hora y 35 minutos (95 minutos) | RF-005, RN-004 |
| CP-011 | Consulta de un vehículo dentro del parqueadero | Vehículo con ingreso activo | Consultar por placa | Muestra datos del vehículo, su tipo de motor y la celda física que ocupa | RF-006 |
| CP-012 | Consulta de un vehículo fuera del parqueadero | Vehículo registrado y fuera | Consultar por placa | Muestra datos del vehículo, tipo de motor y estado *fuera del parqueadero* | RF-006 |
| CP-013 | Integridad de los datos registrados | Un vehículo con ingreso y salida registrados | Consultar vehículo y recorrido | Los datos coinciden con los ingresados, sin alteraciones | RNF-002 |
| CP-014 | Flujo completo integrado | Vehículo sin registrar, disponibilidad inicial D | Registrar vehículo, ingresar, consultar, salir, consultar | La disponibilidad pasa de D a D − 1 y vuelve a D; la permanencia es coherente | Criterios de aceptación 1 a 6 de ESP-001 |
| CP-015 | Registrar vehículo eléctrico con requerimiento de carga [CR-002] | Placa no registrada | Registrar placa, marca, color y seleccionar tipo "Eléctrico" | El vehículo queda almacenado clasificando su naturaleza energética | RF-001 |
| CP-016 | Parametrización e identificación de celda con cargador [CR-002] | El sistema posee un inventario de celdas | Consultar o registrar celdas físicas en el sistema | El sistema identifica unívocamente qué espacios disponen de cargador | RF-007 |
| CP-017 | Asignación prioritaria para vehículo eléctrico [CR-002] | Vehículo eléctrico registrado; celdas con cargador libres | Registrar ingreso del vehículo eléctrico | El sistema asigna automáticamente una celda dotada de cargador | RF-002, RN-005 |
| CP-018 | Asignación automática para vehículo convencional [CR-002] | Vehículo común registrado; celdas comunes libres | Registrar ingreso del vehículo convencional | El sistema asigna automáticamente una celda común sin cargador | RF-002, RN-005 |
| CP-019 | Asignación de celda con cargador por contingencia [CR-002] | Vehículo común registrado; celdas comunes llenas; celdas eléctricas libres | Registrar ingreso del vehículo convencional | El sistema le asigna una celda con cargador para no denegar el servicio | RF-002, RN-005 |
| CP-020 | Rechazo de ingreso eléctrico por falta de cupo compatible [CR-002] | Vehículo eléctrico registrado; celdas con cargador llenas | Registrar ingreso del vehículo eléctrico | El ingreso se rechaza por falta de cupo compatible | RF-002, RN-005 |
| CP-021 | Consulta discriminada de disponibilidad [CR-002] | Parqueadero inicializado con celdas comunes y con cargador | Consultar disponibilidad | El sistema desglosa los cupos de celdas comunes libres y celdas eléctricas libres | RF-004, RN-003 |

## 7. Cobertura de requisitos

| Requisito / Regla | Casos que lo verifican |
|---|---|
| RF-001 | CP-001, CP-002, CP-015 |
| RF-002 | CP-003, CP-004, CP-017, CP-018, CP-019, CP-020 |
| RF-003 | CP-006 |
| RF-004 | CP-008, CP-009, CP-021 |
| RF-005 | CP-010 |
| RF-006 | CP-011, CP-012 |
| RF-007 | CP-016 |
| RN-001 | CP-003, CP-004 |
| RN-002 | CP-005, CP-007 |
| RN-003 | CP-008, CP-009, CP-021 |
| RN-004 | CP-010 |
| RN-005 | CP-017, CP-018, CP-019, CP-020 |
| RNF-002 | CP-013, CP-014 |
| RNF-001 | Inspección de la interfaz y del manual DOC-001 (claridad de las operaciones) |
| RNF-003 | Verificado mediante la matriz de trazabilidad y los registros de gestión, no con un caso de prueba |
| RNF-004 | Revisión de la organización del código y de la documentación |

Todos los requisitos funcionales y reglas de negocio tienen al menos un caso de prueba.

Estado de la prueba: Pendiente de ejecución

