import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image




class Segunda_Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana2 = tk.Tk()
        self.ventana2.title("Datos Generales")
        self.ventana2.geometry("900x600")
        self.ventana2.resizable(False, False)

        # Estilo para los labels
        label_style = {"font": ("Arial", 12)}

        # Label y Entry para el nombre del operador
        self.label1 = tk.Label(self.ventana2, text="Nombre del operador:", **label_style)
        self.label1.place(x=100, y=50)
        self.entry1 = tk.Entry(self.ventana2)
        self.entry1.place(x=100, y=80)

        # Label y Entry para el nombre de la prueba
        self.label2 = tk.Label(self.ventana2, text="Nombre de la prueba:", **label_style)
        self.label2.place(x=300, y=50)
        self.entry2 = tk.Entry(self.ventana2)
        self.entry2.place(x=300, y=80)

        # Label y Entry para el cliente
        self.label3 = tk.Label(self.ventana2, text="Cliente:", **label_style)
        self.label3.place(x=100, y=150)
        self.entry3 = tk.Entry(self.ventana2)
        self.entry3.place(x=100, y=180)

        # Label y Entry para la descripción de la prueba
        self.label4 = tk.Label(self.ventana2, text="Descripción de la prueba:", **label_style)
        self.label4.place(x=300, y=150)
        self.entry4 = tk.Entry(self.ventana2)
        self.entry4.place(x=300, y=180, width=450, height=200)

        self.boton = tk.Button(self.ventana2, text="Guardar", command=self.controlador.guardar_datos_generales,
                               width=15, height=3, bg="#4CAF50", fg="white", font=("Arial", 16, "bold"))

        self.boton.place(x=380, y=450)

    def obtener_datos(self):
        return self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get()

    def confirma_datos(self, val1, val2, val3, val4):
        mensaje = (
            f"Estos son los datos que se van a guardar:"
            f"\n\nNombre del operador: '{val1}'"
            f"\nNombre de la prueba: '{val2}'"
            f"\nCliente: '{val3}'"
            f"\nDescripción de la prueba: '{val4}'"
        )
        return messagebox.askyesno(message=mensaje, title="Ingresar datos")

    def cerrar_ventana2(self):
        self.ventana2.destroy()

    def iniciar(self):
        self.ventana2.mainloop()