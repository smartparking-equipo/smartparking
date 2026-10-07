# ==============================================================================
# ELEMENTO DE CONFIGURACIÓN: SRC-001 - Gestión de Parqueadero Core
# PROYECTO: SmartParking
# VERSIÓN: 1.2
# ESTADO: En modificacion CR-002
# FECHA: 06/10/2026
# RESPONSABLE DEL CI: Equipo SmartParking
# RESPONSABLE DEL CAMBIO: Victorcano19
# ==============================================================================
# Nota de actualización documental — 06/10/2026:
# Se evoluciona el código funcional para dar cumplimiento a la solicitud CR-002.
# Se añade el soporte para identificar vehículos eléctricos y parametrizar
# celdas con cargadores independientes, aplicando lógica de priorización.
# Responsable de la actualización: alexagr210.
# ==============================================================================

from datetime import datetime

class Celda:
    """[CR-001/CR-002] Representa un espacio físico individual en el parqueadero."""
    def __init__(self, identificador, tiene_cargador=False):
        self.identificador = identificador  # Ejemplo: "Celda-01", "Celda-02"
        self.tiene_cargador = tiene_cargador  # [CR-002] Define si cuenta con cargador
        self.vehiculo_ocupante = None       # Guarda el objeto Vehiculo si está ocupada

    @property
    def esta_disponible(self):
        return self.vehiculo_ocupante is None


class Vehiculo:
    """[CR-002] Representa un vehículo registrado en el sistema."""
    def __init__(self, placa, marca, color, tipo_vehiculo="Convencional"):
        self.placa = placa
        self.marca = marca
        self.color = color
        self.tipo_vehiculo = tipo_vehiculo  # "Convencional" o "Eléctrico"


class SmartParking:
    """
    Lógica de control evolucionada para la Línea Base 1.2.
    Soporta asignación automática con segmentación para vehículos eléctricos.
    """
    def __init__(self, diccionario_celdas):
        """
        Inicializa el parqueadero con la estructura física parametrizada.
        diccionario_celdas: Diccionario {'Id_Celda': tiene_cargador (bool)}
        """
        # [CR-002] Creación del mapa físico con distinción de cargadores
        self.celdas = {id_c: Celda(id_c, cargador) for id_c, cargador in diccionario_celdas.items()}
        self.capacidad_total = len(diccionario_celdas)
        # Registro rápido de {placa: (hora_ingreso, objeto_celda, objeto_vehiculo)}
        self.vehiculos_activos = {}

    def _buscar_espacio_disponible(self, tipo_vehiculo):
        """[CR-002] Algoritmo con prioridades y contingencias según RN-005."""
        if tipo_vehiculo == "Eléctrico":
            # Prioridad 1: Buscar celda con cargador disponible
            for celda in self.celdas.values():
                if celda.esta_disponible and celda.tiene_cargador:
                    return celda
            return None  # Vehículo eléctrico no toma común para no forzar reglas

        else:
            # Vehículo Convencional: Buscar celda común disponible primero
            for celda in self.celdas.values():
                if celda.esta_disponible and not celda.tiene_cargador:
                    return celda
            # Contingencia: Si no hay comunes libres, toma una con cargador
            for celda in self.celdas.values():
                if celda.esta_disponible and celda.tiene_cargador:
                    return celda
            return None

    def registrar_ingreso(self, vehiculo):
        """[CR-001/CR-002] Registra el vehículo asignando un espacio según su motor."""
        if vehiculo.placa in self.vehiculos_activos:
            return f"ERROR: El vehículo con placa {vehiculo.placa} ya registra un ingreso activo."

        # Invocar la función de búsqueda automática segmentada [CR-002]
        celda_libre = self._buscar_espacio_disponible(vehiculo.tipo_vehiculo)
        
        if not celda_libre:
            return f"INGRESO RECHAZADO: No hay celdas disponibles para un vehículo de tipo {vehiculo.tipo_vehiculo}."

        # Mutar el estado del componente físico y mapear en activos
        celda_libre.vehiculo_ocupante = vehiculo
        self.vehiculos_activos[vehiculo.placa] = (datetime.now(), celda_libre, vehiculo)
        
        return (f"INGRESO EXITOSO: Vehículo {vehiculo.placa} ({vehiculo.tipo_vehiculo}) registrado. "
                f"Celda asignada automáticamente: {celda_libre.identificador} "
                f"(¿Tiene cargador?: {celda_libre.tiene_cargador})")

    def registrar_salida(self, placa):
        """Libera la celda asignada y calcula el tiempo de permanencia."""
        if placa not in self.vehiculos_activos:
            return f"ERROR: No se encontró un registro de ingreso activo para la placa {placa}."
        
        # Extraer la metadata de control del vehículo activo
        hora_ingreso, celda_asignada, vehiculo = self.vehiculos_activos.pop(placa)
        hora_salida = datetime.now()
        
        # Liberar la ocupación física de la celda
        celda_asignada.vehiculo_ocupante = None
        
        # Cálculo de permanencia en minutos
        diferencia = hora_salida - hora_ingreso
        tiempo_permanencia_minutos = int(diferencia.total_seconds() / 60)
        
        return (f"SALIDA EXITOSA: Vehículo {placa} liberó la celda {celda_asignada.identificador}. "
                f"Tiempo total de permanencia: {tiempo_permanencia_minutos} minutos.")

    def consultar_disponibilidad(self):
        """[CR-002] Devuelve la disponibilidad discriminada del parqueadero."""
        libres_comunes = sum(1 for c in self.celdas.values() if c.esta_disponible and not c.tiene_cargador)
        libres_electricas = sum(1 for c in self.celdas.values() if c.esta_disponible and c.tiene_cargador)
        
        return {
            "disponibles_comunes": libres_comunes,
            "disponibles_electricas": libres_electricas,
            "disponibilidad_global": libres_comunes + libres_electricas
        }


# ==============================================================================
# VERIFICACIÓN LOCAL DE LA SOLICITUD DE CAMBIO (CR-002)
# ==============================================================================
if __name__ == "__main__":
    print("--- CONTROL DE CAMBIOS LOCAL - VERIFICACIÓN DE CR-002 ---")
    
    # Parametrización del parqueadero: 2 celdas comunes y 1 celda con cargador
    estructura_parqueadero = {
        "Cupo-01": False,
        "Cupo-02": False,
        "Electro-01": True  # Espacio con infraestructura de carga [CR-002]
    }
    
    parqueadero_test = SmartParking(estructura_parqueadero)
    print(f"Estado inicial de cupos: {parqueadero_test.consultar_disponibilidad()}")
    
    # Instanciar vehículos de prueba
    carro_comun1 = Vehiculo("XYZ-123", "Mazda", "Gris", "Convencional")
    carro_comun2 = Vehiculo("ABC-456", "Renault", "Rojo", "Convencional")
    carro_electrico = Vehiculo("ELC-789", "BYD", "Blanco", "Eléctrico")
    
    # 1. Probar enrutamiento prioritario eléctrico
    print("\n--- Test 1: Ingreso de vehículo eléctrico ---")
    print(parqueadero_test.registrar_ingreso(carro_electrico))  # Debe ir a Electro-01
    print(parqueadero_test.consultar_disponibilidad())
    
    # 2. Probar enrutamiento convencional
    print("\n--- Test 2: Ingreso de vehículo convencional ---")
    print(parqueadero_test.registrar_ingreso(carro_comun1))  # Debe ir a un Cupo común (01 o 02)
    print(parqueadero_test.consultar_disponibilidad())
    
    # 3. Probar liberación de celdas
    print("\n--- Test 3: Salida del vehículo eléctrico ---")
    print(parqueadero_test.registrar_salida("ELC-789"))
    print(f"Estado final de cupos: {parqueadero_test.consultar_disponibilidad()}")
