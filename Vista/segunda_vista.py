import tkinter as tkinter
import messagebox as messagebox


class Segunda_Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana2 = tkinter.Tk()
        self.ventana2.title("Datos Generales")
        self.ventana2.geometry("900x600")
        self.ventana2.resizable(False, False)

        self.label1 = tkinter.Label(self.ventana2, text="Nombre del operador:")
        self.label1.pack()
        self.label1.place(x=100, y=70)
        self.entry1 = tkinter.Entry(self.ventana2)
        self.entry1.pack()
        self.entry1.place(x=100, y=100)

        self.label2 = tkinter.Label(self.ventana2, text="Nombre de la prueba:")
        self.label2.pack()
        self.label2.place(x=100, y=170)
        self.entry2 = tkinter.Entry(self.ventana2)
        self.entry2.pack()
        self.entry2.place(x=100, y=200)

        self.label3 = tkinter.Label(self.ventana2, text="Cliente:")
        self.label3.pack()
        self.label3.place(x=100, y=270)
        self.entry3 = tkinter.Entry(self.ventana2)
        self.entry3.pack()
        self.entry3.place(x=100, y=300)

        self.label4 = tkinter.Label(self.ventana2, text="Descripcion de la prueba")
        self.label4.pack()
        self.label4.place(x=100, y=370)
        self.entry4 = tkinter.Entry(self.ventana2)
        self.entry4.pack()
        self.entry4.place(x=100, y=400, width=150, height=90)

        self.boton = tkinter.Button(self.ventana2, text="Guardar ", command=self.controlador.guardar_datos_generales())
        self.boton.pack()
        self.boton.place(x=250, y=400)

    def obtener_datos(self):
        return (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get())

    def confirma_datos(self, val1, val2, val3, val4):
        return messagebox.askyesno(message=f"Estos son los datos que se van a guardar "
                                           f"\n Nombre del operador: '{val1}'"
                                           f"\n Nombre de la prueba: '{val2}'"
                                           f"\n Cliente: '{val3}'"
                                           f"\n Descripcion de la prueba: '{val4}'",
                                   title="Ingresar datos")

    def iniciar(self):
        self.ventana2.mainloop()
