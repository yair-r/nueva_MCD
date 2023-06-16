import tkinter as tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as MessageBox
import shutil

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tkinter.Tk()
        self.ventana.title("Ensayo de Corte directo")
        self.ventana.geometry("900x600")
        self.ventana.resizable(False, False)

        self.tree = ttk.Treeview(self.ventana, height=20)
        self.tree["columns"] = ("#1", "#2", "#3")
        self.tree.column("#0", width=60)
        self.tree.column("#1", width=200)
        self.tree.column("#2", width=350)
        self.tree.column("#3", width=150)
        self.tree.heading("#0", text="id")
        self.tree.heading("#1", text="Nombre")
        self.tree.heading("#2", text="Descripción")
        self.tree.heading("#3", text="Fecha")
        self.tree.place(x=70, y=150)

        self.boton = tkinter.Button(self.ventana, text="Nueva Prueba", command='''''', width=25, height=5)
        self.boton.pack()
        self.boton.place(x=360, y=40)

        self.etiqueta_hora = tkinter.Label(self.ventana, font=("Arial", 15))
        self.etiqueta_hora.pack()
        self.etiqueta_hora.place(x=20, y=10)

        def on_tree_select(event):
            item = tree.selection()[0]
            a = tree.set(item)
            nombre = a["#1"]
            fecha = a["#3"]
            obtener_datos_tabla(nombre, fecha)

    def obtener_archivo(self,direccion_arc):
        try:
            file_path = direccion_arc
            path_destino = filedialog.askdirectory()
            shutil.copy(file_path, path_destino)
            bandera = True
        except Exception as err:
            print(err, " ")
            bandera = False
        if bandera:
            MessageBox.showinfo("Archivos de la prueba", "Se ha creo una copia de los archivos en: \n" + path_destino)
        else:
            MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")

    def actualizar_lista_ensayos(self):
        ensayos=self.controlador.obtener_ensayos()
        for row in ensayos:
            self.tree.insert("", "end", text="", values=row)
    def actualizar_hora(self):
        hora_actual = self.controlador.obtener_hora_actual()
        self.etiqueta_hora.config(text=hora_actual)
        self.ventana.after(1000, self.actualizar_hora)

    def iniciar(self):
        self.actualizar_lista_ensayos()
        self.actualizar_hora()
        self.ventana.mainloop()
