
# TST-001 - Plan y Casos de Prueba

## 1. Información del elemento de configuración

| Campo | Información |
|---|---|
| Código | TST-001 |
| Nombre | Plan y casos de prueba |
| Categoría | Pruebas |
| Versión | 1.0 |
| Estado | Pendiente por revisión |
| Sistema | SmartParking - Gestión de Parqueadero |
| Especificación que verifica | ESP-001 v1.0 |
| Código que verifica | SRC-001 v1.0 |

## Control de versiones

| Versión | Fecha | Descripción | Responsable |
|---|---|---|---|
| 1.0 | 2026-10-04 | Creación del plan y los casos de prueba iniciales | Equipo de SmartParking |

## 2. Propósito

Verificar que la versión 1.0 de SmartParking cumple los requisitos y reglas
de negocio de ESP-001, de modo que la línea base inicial sea coherente entre
su especificación, su diseño, su código y su manual.

## 3. Alcance

**Se prueba:** RF-001 a RF-006 y RNF-001 a RNF-004.



## 4. Estrategia

| Aspecto | Definición |
|---|---|
| Tipo de prueba | Funcional, de caja negra, sobre las operaciones del sistema |
| Método | Verificación manual: recorrido del código de SRC-001 y revisión de los documentos contra cada caso |
| Ejecutor | Responsable de pruebas, con apoyo de un segundo integrante |
| Entorno | El definido para la verificación (el sistema debe tener configurada una capacidad de N espacios) |


## 5. Criterios

**Entrada:** los CI de la línea base están completos (ESP-001, DES-001, SRC-001).

**Aceptación:** todos los casos obligatorios se verifican con estado *Aprobado*.
Si algún caso falla, se corrige el CI afectado y se repiten las pruebas antes
de marcar la línea base.

## 6. Casos de prueba

| ID | Caso | Precondición | Pasos / Entrada | Resultado esperado | Requisito / Regla |
|---|---|---|---|---|---|
| CP-001 | Registrar vehículo con datos completos | Placa no registrada | Registrar placa, marca y color | El vehículo queda almacenado con sus datos | RF-001 |
| CP-002 | Registrar vehículo sin un dato obligatorio | Ninguna | Registrar dejando la placa vacía | El sistema no almacena el vehículo y informa el dato faltante | RF-001 |
| CP-003 | Ingreso de vehículo registrado | Vehículo registrado y fuera del parqueadero | Registrar el ingreso con su placa | Se almacena placa, fecha y hora de entrada | RF-002, RN-001 |
| CP-004 | Ingreso de vehículo no registrado | Placa no registrada | Registrar ingreso con esa placa | El ingreso se rechaza con un mensaje | RF-002, RN-001 |
| CP-005 | Segundo ingreso sin haber salido | Vehículo con ingreso activo | Registrar otro ingreso con la misma placa | El ingreso se rechaza | RN-002 |
| CP-006 | Salida de vehículo con ingreso activo | Vehículo con ingreso activo | Registrar la salida con su placa | Se almacena placa, fecha y hora de salida | RF-003|
| CP-007 | Reingreso tras completar la salida | Vehículo que ya registró su salida | Registrar un nuevo ingreso | El ingreso se acepta | RN-002 |
| CP-008 | Disponibilidad tras un ingreso | Disponibilidad inicial conocida (D) | Registrar un ingreso y consultar | La disponibilidad es D − 1 | RF-004, RN-003 |
| CP-009 | Disponibilidad tras una salida | Vehículo con ingreso activo | Registrar la salida y consultar | La disponibilidad aumenta en 1 | RF-004, RN-003 |
| CP-010 | Cálculo del tiempo de permanencia | Ingreso 08:00 y salida 09:35 del mismo día | Consultar el tiempo de permanencia | 1 hora y 35 minutos (95 minutos) | RF-005, RN-004 |
| CP-011 | Consulta de un vehículo dentro del parqueadero | Vehículo con ingreso activo | Consultar por placa | Muestra datos del vehículo y estado *dentro del parqueadero* | RF-006 |
| CP-012 | Consulta de un vehículo fuera del parqueadero | Vehículo registrado y fuera | Consultar por placa | Muestra datos del vehículo y estado *fuera del parqueadero* | RF-006 |
| CP-013| Integridad de los datos registrados | Un vehículo con ingreso y salida registrados | Consultar vehículo y recorrido | Los datos coinciden con los ingresados, sin alteraciones | RNF-002 |
| CP-014 | Flujo completo integrado | Vehículo sin registrar, disponibilidad inicial D | Registrar vehículo, ingresar, consultar, salir, consultar | La disponibilidad pasa de D a D − 1 y vuelve a D; la permanencia es coherente | Criterios de aceptación 1 a 6 de ESP-001 |

## 7. Cobertura de requisitos

| Requisito / Regla | Casos que lo verifican |
|---|---|
| RF-001 | CP-001, CP-002 |
| RF-002 | CP-003, CP-004 |
| RF-003 | CP-006 |
| RF-004 | CP-009, CP-010, CP-015 |
| RF-005 | CP-011, CP-015 |
| RF-006 | CP-012, CP-013 |
| RN-001 | CP-003, CP-004 |
| RN-002 | CP-005, CP-008 |
| RN-003 | CP-009, CP-010 |
| RN-004 | CP-011 |
| RNF-002 | CP-014 |
| RNF-001 | Inspección de la interfaz y del manual DOC-001 (claridad de las operaciones) |
| RNF-003 | Verificado mediante la matriz de trazabilidad y los registros de gestión, no con un caso de prueba |
| RNF-004 | Revisión de la organización del código y de la documentación |

Todos los requisitos funcionales y reglas de negocio tienen al menos un caso de prueba.


