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


    def insertar_direccion(self):
        self.nombre = self.vista_pestaña1.obtener_nombreArchivo()
        temporal = "C:/Users/Yair/Desktop/Nuvo_nuevo_MCD/"
        direccion = temporal + self.nombre
        self.modelo.insertar_direccion(direccion)

    def generar_pdf(self):
       temporal=[]
       tree =  self.vista_pestaña1.tree1
       nombre =self.vista_pestaña1.obtener_nombreArchivo()
       temporal=self.modelo.obterner_ultimoregistro()
       id_valor = temporal[0][0]
       nombre_operador = temporal[0][1]
       nombre_prueba = temporal[0][2]
       descripcion = temporal[0][3]
       cliente = temporal[0][4]
       fecha = temporal[0][5]
       self.modelo.generar_pdf(tree,nombre,id_valor,nombre_operador,nombre_prueba,descripcion,cliente,fecha)
       self.insertar_direccion()
       self.abrir_denuevomenu()

    def cargar_valoresgrafica(self):
        valores_x,valores_y =self.modelo.cargar_archivo()

    def ingresar_esfuerzocortantearchivo(self, indice, datos):
        contenido=None
        if indice == 1:
            with open('datos1.txt','r') as file:
                contenido = file.readlines()
        elif indice == 2:
            with open('datos2.txt','r') as file:
                contenido = file.readlines()
        elif indice == 3:
            with open('datos3.txt','r') as file:
                contenido = file.readlines()

        if len(datos) != len(contenido):
            print("El tamaño del arreglo no coincide con el número de filas existentes.")
        else:
            filas_actualizadas = []
            for i in range(len(contenido)):
                fila = contenido[i].strip()
                valor_columna = datos[i]
                fila_actualizada = fila + ", " + str(valor_columna) + "\n"
                filas_actualizadas.append(fila_actualizada)

            contenido_actualizado = ''.join(filas_actualizadas)

            if indice == 1:
                with open('datos1.txt', 'w') as file:
                    file.write(contenido_actualizado)
            elif indice == 2:
                with open('datos2.txt', 'w') as file:
                    file.write(contenido_actualizado)
            elif indice == 3:
                with open('datos3.txt', 'w') as file:
                    file.write(contenido_actualizado)

    def calcular_elmayoresfuerzocortante(self, datos):

        return 3

    def resolver_esfuerzonormal(self):

        return "a"

    def resolver_esfuerzocortante(self, fuerzacostrante, indice):
        datos = None

        if indice == 1:
            datos = self.tercer_vista.obtener_datosPage1()
        elif indice == 2:
            datos = self.tercer_vista.obtener_datosPage2()
        elif indice == 3:
            datos = self.tercer_vista.obtener_datosPage3()

        area = float(datos[1])
        print(area)
        fc = float(fuerzacostrante)
        esfuerzocortante = fc / area
        print(esfuerzocortante)
        return esfuerzocortante

    def calcular_esfuerzocortante1(self):
        fuerzacortante = []
        esfuerzocortante = []
        datos = self.tercer_vista.recuperar_datosTabla1()
        for data in datos:
            temporal = data[0]
            fuerzacortante.append(temporal)
        for dato in fuerzacortante:
            res = self.resolver_esfuerzocortante(dato, 1)
            esfuerzocortante.append(res)

        print(esfuerzocortante)
        self.ingresar_esfuerzocortantearchivo(1,esfuerzocortante)

    def calcular_esfuerzocortante2(self):
        fuerzacortante = []
        esfuerzocortante = []
        datos = self.tercer_vista.recuperar_datosTabla2()
        for data in datos:
            temporal = data[0]
            fuerzacortante.append(temporal)
        for dato in fuerzacortante:
            res = self.resolver_esfuerzocortante(dato, 2)
            esfuerzocortante.append(res)

        print(esfuerzocortante)
        self.ingresar_esfuerzocortantearchivo(2,esfuerzocortante)

    def calcular_esfuerzocortante3(self):
        fuerzacortante = []
        esfuerzocortante = []
        datos = self.tercer_vista.recuperar_datosTabla3()
        for data in datos:
            temporal = data[0]
            fuerzacortante.append(temporal)
        for dato in fuerzacortante:
            res = self.resolver_esfuerzocortante(dato, 3)
            esfuerzocortante.append(res)

        print(esfuerzocortante)
        self.ingresar_esfuerzocortantearchivo(3,esfuerzocortante)

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

    def agregar_datosarbolpestaña1(self):
        datos = self.modelo.leer_archivo1()
        self.vista_pestaña1.agregar_datosarbolpestaña1(datos)
    def abrir_graficasPestaña1(self):
        self.vista_pestaña1 = Vista_Pestaña1(self)
        self.tercer_vista.cerrar_pestaña()
        self.agregar_datosarbolpestaña1()
        #self.cargar_valoresgrafica()

    def abrir_denuevomenu(self):
        self.ejecutar()
        self.vista_pestaña1.cerrar_pestaña()

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
                self.modelo.ingresar_datos_generales(val1, val2, val3, val4)
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
        return self.datos

    def obtener_hora_actual(self):
        return self.modelo.obtener_hora_actual()

    def ejecutar(self):
        self.vista.iniciar()
