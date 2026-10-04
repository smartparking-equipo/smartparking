# ==============================================================================
# ELEMENTO DE CONFIGURACIÓN: SRC-001 - Gestión de Parqueadero Core
# PROYECTO: SmartParking
# VERSIÓN: 1.0
# ESTADO: En modificación (Pendiente de revisión y aprobación)
# FECHA: 04/10/2026
# RESPONSABLE DEL CI: Equipo SmartParking
# RESPONSABLE DEL CAMBIO: Alexandra Giraldo Roman
# ==============================================================================

from datetime import datetime

class SmartParking:
    """
    Lógica de control inicial para el Producto Mínimo Inicial de SmartParking.
    Permite registrar vehículos, ingresos, salidas y calcular la permanencia.
    """
    def __init__(self, capacidad_total):
        self.capacidad_total = capacidad_total
        # Estructura inicial: diccionario para mapear {placa: hora_ingreso_datetime}
        self.vehiculos_activos = {}

    def registrar_ingreso(self, placa):
        """Registra la placa de un vehículo y guarda su marca de tiempo de entrada."""
        # Validación de duplicados en el estado activo
        if placa in self.vehiculos_activos:
            return f"ERROR: El vehículo con placa {placa} ya se encuentra dentro del parqueadero."
        
        # Validación de cupo global (Línea Base 1.0)
        if len(self.vehiculos_activos) >= self.capacidad_total:
            return "INGRESO RECHAZADO: No hay celdas globales disponibles en este momento."
        
        # Captura de la hora de ingreso en tiempo real
        self.vehiculos_activos[placa] = datetime.now()
        return f"INGRESO EXITOSO: Vehículo {placa} registrado correctamente."

    def registrar_salida(self, placa):
        """Libera el espacio del vehículo y calcula el tiempo de permanencia exacto."""
        if placa not in self.vehiculos_activos:
            return f"ERROR: No se encontró un registro de ingreso activo para la placa {placa}."
        
        # Extraer la marca de tiempo de entrada y remover del parqueadero activo
        hora_ingreso = self.vehiculos_activos.pop(placa)
        hora_salida = datetime.now()
        
        # Cálculo preciso de la permanencia convertido a minutos
        diferencia = hora_salida - hora_ingreso
        tiempo_permanencia_minutos = int(diferencia.total_seconds() / 60)
        
        return (f"SALIDA EXITOSA: Vehículo {placa} ha salido del parqueadero. "
                f"Tiempo total de permanencia: {tiempo_permanencia_minutos} minutos.")

    def consultar_disponibilidad(self):
        """Consulta matemática simple de cupos libres totales basados en la capacidad."""
        cupos_ocupados = len(self.vehiculos_activos)
        cupos_disponibles = self.capacidad_total - cupos_ocupados
        return cupos_disponibles


# ==============================================================================
# REVISIÓN DE COHERENCIA CON LA LÍNEA BASE INICIAL (BL-001)
# ==============================================================================
if __name__ == "__main__":
    # Simulación del estado base sin automatizaciones para pruebas locales
    print("--- CONTROL DE CONFIGURACIÓN LOCAL - VERIFICACIÓN REQ VS SRC ---")
    
    # Parqueadero universitario con capacidad inicial de 50 puestos globales
    parqueadero_test = SmartParking(capacidad_total=50)
    
    # 1. Verificar lectura de disponibilidad inicial (Debe coincidir con la capacidad)
    print(f"Cupos libres al inicializar: {parqueadero_test.consultar_disponibilidad()}")
    
    # 2. Simular un flujo básico de ingreso
    print(parqueadero_test.registrar_ingreso("UCP-123"))
    print(f"Cupos libres tras un ingreso: {parqueadero_test.consultar_disponibilidad()}")
    
    # 3. Simular salida inmediata (Tiempo esperado: 0 minutos)
    print(parqueadero_test.registrar_salida("UCP-123"))
    print(f"Cupos libres tras la salida: {parqueadero_test.consultar_disponibilidad()}")
