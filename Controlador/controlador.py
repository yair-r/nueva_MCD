from Modelo.modelo import Modelo
from Vista.vista import Vista


class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(self)

    def obtener_ensayos(self):
        self.datos = self.modelo.obtener_datos_pruebas()
        self.modelo.cerrar_conexion()
        return self.datos

    def obtener_hora_actual(self):
        return self.modelo.obtener_hora_actual()

    def ejecutar(self):
        self.vista.iniciar()
