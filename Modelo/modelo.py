import time
import mysql.connector
from tkinter import filedialog
import shutil


class Modelo:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            port='3306',
            host="localhost",
            user="admin",
            password="admin",
            database="sistema_mcd"
        )
    def ingresar_datos_generales(self, val1, val2, val3, val4):
        val5= self.obtener_hora_actual()
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

    def cerrar_conexion(self):
        self.mydb.close()

    def obtener_hora_actual(self):
        return time.strftime("%d-%m-%Y %H:%M")