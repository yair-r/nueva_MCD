import tkinter as tkinter
from tkinter import ttk
from tkinter import messagebox as MessageBox


class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tkinter.Tk()
        self.ventana.title("Ensayo de Corte directo")
        self.ventana.geometry("900x600")
        self.ventana.resizable(False, False)

        style = ttk.Style()
        style.theme_use("default")  # Usa el tema predeterminado de ttk

        # Configuración de las propiedades del estilo "Treeview"
        style.configure("Treeview",
                        background="#eaf2f8",  # Color de fondo
                        foreground="black",  # Color de texto
                        rowheight=25,  # Altura de fila
                        font=("Arial", 10))  # Fuente y tamaño de texto

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

        self.boton = tkinter.Button(self.ventana, text="Nueva Prueba", command=self.controlador.abrir_segundaVentana,
                                    width=25, height=5, borderwidth=2, font=("Arial", 12),  bg="orange", fg="white")
        self.boton.pack()
        self.boton.place(x=350, y=40)

        self.etiqueta_hora = tkinter.Label(self.ventana, font=("Arial", 15))
        self.etiqueta_hora.pack()
        self.etiqueta_hora.place(x=20, y=10)

        texto = "Software maquina de corte directo\n CeVIDE-CRODE Celaya"
        self.label33 = tkinter.Label(self.ventana, text=texto, font=("Arial", 13))
        self.label33.pack()
        self.label33.place(x=620,y=10)


    def mostrar_copia_archivo(self, path_destino):
        MessageBox.showinfo("Archivos de la prueba", "Se ha creado una copia de los archivos en: \n" + path_destino)

    def mostrar_error_archivo(self):
        MessageBox.showerror("Error", "Ha ocurrido un error inesperado.")

    def actualizar_lista_ensayos(self):
        ensayos = self.controlador.obtener_ensayos()
        for row in ensayos:
            self.tree.insert("", "end", text="", values=row)

    def cerrar_ventana(self):
        self.ventana.destroy()

    def actualizar_hora(self):
        hora_actual = self.controlador.obtener_hora_actual()
        self.etiqueta_hora.config(text=hora_actual)
        self.ventana.after(1000, self.actualizar_hora)

    def iniciar(self):
        self.actualizar_lista_ensayos()
        self.actualizar_hora()
        self.ventana.mainloop()