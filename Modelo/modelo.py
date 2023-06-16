import time
import mysql.connector


class Modelo:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            port='3306',
            host="localhost",
            user="admin",
            password="admin",
            database="sistema_mcd"
        )

    def selecionar_archivos(self, nombre, fecha):
        mycursor = self.mydb.cursor()
        mycursor.execute(
            "select direccion_archivos from historial_pruebas where fecha='{x}'and nombre_prueba='{}'".format(fecha,nombre))
        res = mycursor.fetchall()
        direccion_archivo = ''.join(res[0])
        return direccion_archivo



    def obtener_datos_pruebas(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("select nombre_prueba,descripcion,fecha from historial_pruebas;")
        return mycursor.fetchall()

    def cerrar_conexion(self):
        self.mydb.close()

    def obtener_hora_actual(self):
        return time.strftime("%d-%m-%Y %H:%M")
