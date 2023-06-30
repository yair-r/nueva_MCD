from Vista.vista_pestaña1 import Vista_Pestaña1
from Vista.vista_pestaña2 import Vista_Pestaña2
from Vista.vista_pestaña3 import Vista_Pestaña3
from Vista.segunda_vista import Segunda_Vista
from Vista.tercer_vista import Tercer_Vista
from Modelo.modelo import Modelo
from Vista.vista import Vista


class Controlador:
    def __init__(self):

        self.modelo = Modelo()
        self.vista = Vista(self)
        self.segunda_vista = None
        self.tercer_vista = None
        self.vista_pestaña1 = None
        self.vista_pestaña2 = None
        self.vista_pestaña3 = None

        self.vista.tree.bind("<Double-Button-1>", self.on_tree_select)

    def agregar_datosTree3(self):
        datos = self.modelo.leer_archivo3()
        self.tercer_vista.agregar_datosTree3(datos)

    def agregar_datosTree2(self):
        datos = self.modelo.leer_archivo2()
        self.tercer_vista.agregar_datosTree2(datos)

    def agregar_datosTree1(self):
        datos = self.modelo.leer_archivo1()
        self.tercer_vista.agregar_datosTree1(datos)

    def abrir_graficasPestaña3(self):
        self.vista_pestaña3 = Vista_Pestaña3(self)
        self.tercer_vista.cerrar_pestaña()

    def abrir_graficasPestaña2(self):
        self.vista_pestaña2 = Vista_Pestaña2(self)
        self.tercer_vista.cerrar_pestaña()

    def abrir_graficasPestaña1(self):
        self.vista_pestaña1 = Vista_Pestaña1(self)
        self.tercer_vista.cerrar_pestaña()

    def abrir_tercerVentana(self):
        self.tercer_vista = Tercer_Vista(self)
        self.segunda_vista.cerrar_ventana2()

    def abrir_segundaVentana(self):
        self.segunda_vista = Segunda_Vista(self)
        self.vista.cerrar_ventana()

    def guardar_datos_generales(self):
        if self.segunda_vista:
            val1, val2, val3, val4 = self.segunda_vista.obtener_datos()
            resultado = self.segunda_vista.confirma_datos(val1, val2, val3, val4)

            if resultado == True:
                '''self.modelo.ingresar_datos_generales(val1, val2, val3, val4)'''
                self.abrir_tercerVentana()
            else:
                print("Error de guardado")
                self.segunda_vista.cerrar_ventana2()
        else:
            print("La segunda vista no ha sido inicializada")
            self.segunda_vista.cerrar_ventana2()

    def on_tree_select(self, event):
        item = self.vista.tree.selection()[0]
        a = self.vista.tree.set(item)
        nombre = a["#1"]
        fecha = a["#3"]
        direccion_archivo = self.modelo.obtener_datos_tabla(nombre, fecha)
        self.obtener_archivo(direccion_archivo)

    def obtener_archivo(self, direccion_archivo):
        bandera, path_destino = self.modelo.obtener_archivo(direccion_archivo)

        if bandera:
            self.vista.mostrar_copia_archivo(path_destino)
        else:
            self.vista.mostrar_error_archivo()

    def obtener_ensayos(self):
        self.datos = self.modelo.obtener_datos_pruebas()
        self.modelo.cerrar_conexion()
        return self.datos

    def obtener_hora_actual(self):
        return self.modelo.obtener_hora_actual()

    def ejecutar(self):
        self.vista.iniciar()