# ==============================================================================
# ELEMENTO DE CONFIGURACIÓN: SRC-001 - Gestión de Parqueadero Core
# PROYECTO: SmartParking
# VERSIÓN: 1.1
# ESTADO: Aprobado
# FECHA: 04/10/2026
# RESPONSABLE DEL CI: Equipo SmartParking
# RESPONSABLE DEL CAMBIO: Alexagr2110
# ==============================================================================
# Nota de actualización documental — 06/10/2026:
# Se actualiza el estado de SRC-001 a Aprobado, conforme a la aprobación
# de CR-001 registrada por Revant11y, ya integrado en main.
# Se conserva la versión 1.1 y el código funcional.
# Responsable de la actualización: SaraArias801.
# ==============================================================================

from datetime import datetime

class Celda:
    """[CR-001] Representa un espacio físico individual en el parqueadero."""
    def __init__(self, identificador):
        self.identificador = identificador  # Ejemplo: "Celda-01", "Celda-02"
        self.vehiculo_ocupante = None       # Guarda la placa del carro si está ocupada

    @property
    def esta_disponible(self):
        return self.vehiculo_ocupante is None


class SmartParking:
    """
    Lógica de control evolucionada para la Línea Base 1.1.
    Modificada para soportar el mapeo físico y asignación automática de celdas.
    """
    def __init__(self, lista_identificadores):
        """
        Inicializa el parqueadero con un listado estructurado de espacios físicos.
        lista_identificadores: Lista de strings ['Celda-01', 'Celda-02', ...]
        """
        # Creación del mapa físico de celdas del parqueadero
        self.celdas = {id_c: Celda(id_c) for id_c in lista_identificadores}
        self.capacidad_total = len(lista_identificadores)
        # Diccionario de auditoría rápida para mapear {placa: (hora_ingreso, objeto_celda)}
        self.vehiculos_activos = {}

    def _buscar_espacio_disponible(self):
        """[CR-001] Algoritmo interno para encontrar la primera celda libre."""
        for celda in self.celdas.values():
            if celda.esta_disponible:
                return celda
        return None

    def registrar_ingreso(self, placa):
        """[CR-001] Registra el vehículo y le asigna un espacio automáticamente."""
        if placa in self.vehiculos_activos:
            return f"ERROR: El vehículo con placa {placa} ya registra un ingreso activo."

        # Invocar la función de búsqueda automática de celdas libres
        celda_libre = self._buscar_espacio_disponible()
        
        if not celda_libre:
            return "INGRESO RECHAZADO: No hay celdas físicas disponibles en este momento."

        # Mutar el estado físico de la celda y guardarlo en el mapa de control
        celda_libre.vehiculo_ocupante = placa
        self.vehiculos_activos[placa] = (datetime.now(), celda_libre)
        
        return (f"INGRESO EXITOSO: Vehículo {placa} registrado. "
                f"Celda asignada automáticamente: {celda_libre.identificador}")

    def registrar_salida(self, placa):
        """Modificado para liberar el espacio de la celda asignada y calcular permanencia."""
        if placa not in self.vehiculos_activos:
            return f"ERROR: No se encontró un registro de ingreso activo para la placa {placa}."
        
        # Extraer la metadata de control del vehículo activo
        hora_ingreso, celda_asignada = self.vehiculos_activos.pop(placa)
        hora_salida = datetime.now()
        
        # [CR-001] Liberar el recurso físico para que quede disponible para otros usuarios
        celda_asignada.vehiculo_ocupante = None
        
        # Cálculo de permanencia en minutos (Mantenido de la Línea Base 1.0)
        diferencia = hora_salida - hora_ingreso
        tiempo_permanencia_minutos = int(diferencia.total_seconds() / 60)
        
        return (f"SALIDA EXITOSA: Vehículo {placa} liberó la celda {celda_asignada.identificador}. "
                f"Tiempo total de permanencia: {tiempo_permanencia_minutos} minutes.")

    def consultar_disponibilidad(self):
        """Modificado para contar de manera exacta las celdas desocupadas."""
        cupos_libres = sum(1 for celda in self.celdas.values() if celda.esta_disponible)
        return cupos_libres


# ==============================================================================
# VERIFICACIÓN LOCAL DE LA SOLICITUD DE CAMBIO (CR-001)
# ==============================================================================
if __name__ == "__main__":
    print("--- CONTROL DE CAMBIOS LOCAL - VERIFICACIÓN DE CR-001 ---")
    
    # Simulación de un parqueadero con 3 celdas fijas nominadas
    puestos_campus = ["Cupo-01", "Cupo-02", "Cupo-03"]
    parqueadero_test = SmartParking(puestos_campus)
    
    print(f"Disponibilidad inicial de celdas: {parqueadero_test.consultar_disponibilidad()}")
    
    # Verificar la función de asignación automática secuencial
    print(parqueadero_test.registrar_ingreso("UCP-888"))  # Debe tomar Cupo-01
    print(parqueadero_test.registrar_ingreso("XYZ-999"))  # Debe tomar Cupo-02
    
    print(f"Disponibilidad intermedia de celdas: {parqueadero_test.consultar_disponibilidad()}")
    
    # Probar la liberación física del espacio asignado
    print(parqueadero_test.registrar_salida("UCP-888"))   # Libera Cupo-01
    print(f"Disponibilidad final de celdas: {parqueadero_test.consultar_disponibilidad()}")

