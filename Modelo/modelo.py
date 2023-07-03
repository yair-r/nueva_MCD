import time
import mysql.connector
from tkinter import filedialog
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Modelo:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            port='3306',
            host="localhost",
            user="admin",
            password="admin",
            database="sistema_mcd"
        )
        self.x_values = []
        self.y_values = []

    def insertar_direccion(self, nueva_direccion_archivos):
        mycursor = self.mydb.cursor()
        query = "UPDATE historial_pruebas AS h1 " \
                "JOIN (SELECT MAX(numero_prueba) AS max_numero_prueba FROM historial_pruebas) AS h2 " \
                "ON h1.numero_prueba = h2.max_numero_prueba " \
                "SET h1.direccion_archivos = %s;"
        mycursor.execute(query, (nueva_direccion_archivos,))
        self.mydb.commit()
    def obterner_ultimoregistro(self):
        self.mydb.connect()
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM historial_pruebas WHERE numero_prueba = (SELECT MAX(numero_prueba) FROM historial_pruebas);")
        return mycursor.fetchall()

    def generar_pdf(self,treeview, filename, id_valor, nombre_operador, nombre_prueba, descripcion, cliente, fecha):
        # Crear el documento PDF
        c = canvas.Canvas(filename, pagesize=letter)

        # Establecer márgenes y dimensiones de las celdas
        margen_x = 50
        margen_y = 50
        ancho_total = 750
        alto_total = 700
        tamaño_fuente = 12
        alto_celda = 20

        # Escribir los datos en el PDF
        c.setFont("Helvetica", tamaño_fuente)
        c.drawString(margen_x, alto_total - margen_y, "ID: " + str(id_valor))
        c.drawString(margen_x, alto_total - margen_y - tamaño_fuente, "Operador: " + nombre_operador)
        c.drawString(margen_x, alto_total - margen_y - 2 * tamaño_fuente, "Prueba: " + nombre_prueba)
        c.drawString(margen_x, alto_total - margen_y - 3 * tamaño_fuente, "Descripción: " + descripcion)
        c.drawString(margen_x, alto_total - margen_y - 4 * tamaño_fuente, "Cliente: " + cliente)
        c.drawString(margen_x, alto_total - margen_y - 5 * tamaño_fuente, "Fecha: " + fecha)

        # Obtener las columnas del treeview
        columnas = treeview["columns"]
        # Obtener los encabezados
        encabezados = []
        for columna in columnas:
            encabezados.append(treeview.heading(columna)["text"])

        # Obtener los datos de las filas
        filas = []
        for item in treeview.get_children():
            fila = []
            for columna in columnas:
                fila.append(treeview.item(item, "values")[columnas.index(columna)])
            filas.append(fila)

        # Calcular las dimensiones de las celdas
        ancho_celda = (ancho_total - 2 * margen_x) / len(encabezados)

        # Dibujar los encabezados
        c.setFont("Helvetica-Bold", tamaño_fuente)
        for i, encabezado in enumerate(encabezados):
            x = margen_x + i * ancho_celda
            y = alto_total - 2 * margen_y - 5 * tamaño_fuente
            c.drawString(x, y, encabezado)

        # Dibujar las filas
        c.setFont("Helvetica", tamaño_fuente)
        for i, fila in enumerate(filas):
            for j, valor in enumerate(fila):
                x = margen_x + j * ancho_celda
                y = alto_total - 2 * margen_y - (i + 4) * tamaño_fuente - (i + 3) * alto_celda
                c.drawString(x, y, valor)

        # Guardar el documento PDF
        c.save()

    def cargar_archivo(self):
        x_values = []
        y_values = []
        with open('datos1.txt', 'r') as file:
            for line in file:
                values = line.strip().split(',')
                x_values.append(float(values[0]))
                y_values.append(float(values[3]))

        return x_values,y_values

    def leer_archivo3(self):
        with open("datos3.txt", 'r') as file:
            lineas = file.readlines()

        datos = []
        for linea in lineas:
            linea = linea.strip()
            columnas = linea.split(',')
            datos.append(columnas)

        return datos

    def leer_archivo2(self):
        with open("datos2.txt", 'r') as file:
            lineas = file.readlines()

        datos = []
        for linea in lineas:
            linea = linea.strip()
            columnas = linea.split(',')
            datos.append(columnas)

        return datos

    def leer_archivo1(self):
        with open("datos1.txt", 'r') as file:
            lineas = file.readlines()

        datos = []
        for linea in lineas:
            linea = linea.strip()
            columnas = linea.split(',')
            datos.append(columnas)

        return datos

    def ingresar_datos_generales(self, val1, val2, val3, val4):
        val5 = self.obtener_hora_actual()
        self.mydb.connect()
        mycursor = self.mydb.cursor()
        consulta = "insert into historial_pruebas(nombre_operador, nombre_prueba, descripcion, cliente, fecha) values (%s, %s, %s, %s,%s)"
        valores = (val1, val2, val3, val4, val5)
        try:
            mycursor.execute(consulta, valores)
            self.mydb.commit()
        except:
            self.mydb.rollback()
        self.mydb.close()

    def obtener_datos_tabla(self, nombre, fecha):
        self.mydb.connect()
        mycursor = self.mydb.cursor()
        mycursor.execute(
            "SELECT direccion_archivos FROM historial_pruebas WHERE fecha=%(fecha)s AND nombre_prueba=%(nombre)s",
            {"fecha": fecha, "nombre": nombre}
        )
        res = mycursor.fetchall()
        direccion_archivo = ''.join(res[0])
        return direccion_archivo

    def obtener_archivo(self, direccion_arc):
        try:
            file_path = direccion_arc
            path_destino = filedialog.askdirectory()
            shutil.copy(file_path, path_destino)
            return True, path_destino
        except Exception as err:
            print(err, " ")
            return False, ""

    def obtener_datos_pruebas(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("select nombre_prueba,descripcion,fecha from historial_pruebas;")
        return mycursor.fetchall()

    def obtener_hora_actual(self):
        return time.strftime("%d-%m-%Y %H:%M")