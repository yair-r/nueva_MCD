import time
import tkinter as tkinter
from tkinter import ttk


class Tercer_Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana3 = tkinter.Tk()
        self.ventana3.title("Ensayo")
        self.ventana3.geometry("900x600")
        self.ventana3.resizable(False, False)

        self.nb = ttk.Notebook(self.ventana3)
        self.page1 = ttk.Frame(self.nb)
        self.page2 = ttk.Frame(self.nb)
        self.page3 = ttk.Frame(self.nb)

        self.nb.add(self.page1, text='Ensayo No. 1')
        self.nb.add(self.page2, text='Ensayo No. 2')
        self.nb.add(self.page3, text='Ensayo No. 3')

        self.nb.pack(expand=True, fill='both')

        # -----------------------------------------------------------------------

        self.label11 = tkinter.Label(self.page1, text="Forma del molde de corte")
        self.label11.pack()
        self.label11.place(x="15", y="10")
        self.options_list1 = ["Cuadrado", "Cilindro"]
        self.value_inside1 = tkinter.StringVar(self.page1)
        self.value_inside1.set("Molde")
        self.question_menu1 = tkinter.OptionMenu(self.page1, self.value_inside1, *self.options_list1)
        self.question_menu1.pack()
        self.question_menu1.place(x="15", y="30")

        self.label21 = tkinter.Label(self.page1, text="Dimenciones ( Caja - Area | Cilindro - Diametro )")
        self.label21.pack()
        self.label21.place(x="170", y="10")
        self.entry11 = tkinter.Entry(self.page1)
        self.entry11.pack()
        self.entry11.place(x="170", y="30")
        self.label31 = tkinter.Label(self.page1, text="Velocidad de Corte mm/min")
        self.label31.pack()
        self.label31.place(x="460", y="10")
        self.entry21 = tkinter.Entry(self.page1)
        self.entry21.pack()
        self.entry21.place(x="460", y="30")

        self.label51 = tkinter.Label(self.page1, text="Fuerza Normal")
        self.label51.pack()
        self.label51.place(x="630", y="10")
        self.entry41 = tkinter.Entry(self.page1)
        self.entry41.pack()
        self.entry41.place(x="630", y="30")

        self.label61 = tkinter.Label(self.page1, text="  Nombre clave \n de la prueba")
        self.label61.pack()
        self.label61.place(x="780", y="10")
        self.label71 = tkinter.Label(self.page1, text="     ...")
        self.label71.pack()
        self.label71.place(x="780", y="40")

        self.boton11 = tkinter.Button(self.page1, text="Iniciar", command=self.controlador.agregar_datosTree1, width=15, height=5)
        self.boton11.pack()
        self.boton11.place(x="760", y="150")

        self.boton21 = tkinter.Button(self.page1, text="Generar Graficas ", command=self.controlador.abrir_graficasPestaña1, width=15, height=5)
        self.boton21.pack()
        self.boton21.place(x="760", y="270")

        self.boton31 = tkinter.Button(self.page1, text="Parar Prueba", command="", width=15, height=5)
        self.boton31.pack()
        self.boton31.place(x="760", y="390")

        self.tree1 = ttk.Treeview(self.page1, height=20)
        self.tree1['columns'] = ('Columna1', 'Columna2', 'Columna3')
        
        self.tree1.heading('#0', text='Índice')
        self.tree1.column('#0', anchor=tkinter.CENTER, width=80)
        self.tree1.heading('Columna1', text='Fuerza Horizontal \n N')
        self.tree1.column('Columna1', anchor=tkinter.CENTER, width=170)
        self.tree1.heading('Columna2', text='Desplazamiento Horizontal \n mm')
        self.tree1.column('Columna2', anchor=tkinter.CENTER, width=170)
        self.tree1.heading('Columna3', text='Desplazamiento Vertical \n mm')
        self.tree1.column('Columna3', anchor=tkinter.CENTER, width=170)
        self.tree1.pack()
        self.tree1.place(x=80, y=100)

        # ----------------------------------------------------------------------

        self.label12 = tkinter.Label(self.page2, text="Molde de Corte")
        self.label12.pack()
        self.label12.place(x="15", y="10")
        self.options_list2 = ["Cuadrado", "Cilindro"]
        self.value_inside2 = tkinter.StringVar(self.page2)
        self.value_inside2.set("Molde")
        self.question_menu2 = tkinter.OptionMenu(self.page2, self.value_inside2, *self.options_list2)
        self.question_menu2.pack()
        self.question_menu2.place(x="15", y="30")

        self.label22 = tkinter.Label(self.page2, text="Dimenciones ( Caja - Area | Cilindro - Diametro )")
        self.label22.pack()
        self.label22.place(x="170", y="10")
        self.entry12 = tkinter.Entry(self.page2)
        self.entry12.pack()
        self.entry12.place(x="170", y="30")

        self.label32 = tkinter.Label(self.page2, text="Velocidad de Corte mm/min")
        self.label32.pack()
        self.label32.place(x="460", y="10")
        self.entry22 = tkinter.Entry(self.page2)
        self.entry22.pack()
        self.entry22.place(x="460", y="30")

        self.label52 = tkinter.Label(self.page2, text="Fuerza Normal")
        self.label52.pack()
        self.label52.place(x="630", y="10")
        self.entry42 = tkinter.Entry(self.page2)
        self.entry42.pack()
        self.entry42.place(x="630", y="30")

        self.label62 = tkinter.Label(self.page2, text="  Nombre clave \n de la prueba")
        self.label62.pack()
        self.label62.place(x="780", y="10")
        self.label72 = tkinter.Label(self.page1, text="     ...")
        self.label72.pack()
        self.label72.place(x="780", y="40")

        self.boton12 = tkinter.Button(self.page2, text="Iniciar", command=self.controlador.agregar_datosTree2, width=15, height=5)
        self.boton12.pack()
        self.boton12.place(x="760", y="150")

        self.boton22 = tkinter.Button(self.page2, text="Generar Graficas ", command=self.controlador.abrir_graficasPestaña2, width=15, height=5)
        self.boton22.pack()
        self.boton22.place(x="760", y="270")

        self.boton32 = tkinter.Button(self.page2, text="Parar Prueba", command="", width=15, height=5)
        self.boton32.pack()
        self.boton32.place(x="760", y="390")

        self.tree2 = ttk.Treeview(self.page2, height=20)
        self.tree2['columns'] = ('Columna1', 'Columna2', 'Columna3')

        self.tree2.heading('#0', text='Índice')
        self.tree2.column('#0', anchor=tkinter.CENTER, width=80)
        self.tree2.heading('Columna1', text='Fuerza Horizontal')
        self.tree2.column('Columna1', anchor=tkinter.CENTER, width=170)
        self.tree2.heading('Columna2', text='Desplazamiento Horizontal')
        self.tree2.column('Columna2', anchor=tkinter.CENTER, width=170)
        self.tree2.heading('Columna3', text='Desplazamiento Vertical')
        self.tree2.column('Columna3', anchor=tkinter.CENTER, width=170)
        self.tree2.pack()
        self.tree2.place(x=80, y=100)

        # ----------------------------------------------------------------------

        self.label13 = tkinter.Label(self.page3, text="Molde de Corte")
        self.label13.pack()
        self.label13.place(x="15", y="10")
        self.options_list3 = ["Cuadrado", "Cilindro"]
        self.value_inside3 = tkinter.StringVar(self.page3)
        self.value_inside3.set("Molde")
        self.question_menu3 = tkinter.OptionMenu(self.page3, self.value_inside3, *self.options_list3)
        self.question_menu3.pack()
        self.question_menu3.place(x="15", y="30")

        self.label23 = tkinter.Label(self.page3, text="Dimenciones ( Caja - Area | Cilindro - Diametro )")
        self.label23.pack()
        self.label23.place(x="170", y="10")
        self.entry13 = tkinter.Entry(self.page3)
        self.entry13.pack()
        self.entry13.place(x="170", y="30")
        self.label33 = tkinter.Label(self.page3, text="Velocidad de Corte mm/min")
        self.label33.pack()
        self.label33.place(x="460", y="10")
        self.entry23 = tkinter.Entry(self.page3)
        self.entry23.pack()
        self.entry23.place(x="460", y="30")

        self.label53 = tkinter.Label(self.page3, text="Fuerza Normal")
        self.label53.pack()
        self.label53.place(x="630", y="10")
        self.entry43 = tkinter.Entry(self.page3)
        self.entry43.pack()
        self.entry43.place(x="630", y="30")

        self.label63 = tkinter.Label(self.page3, text="  Nombre clave \n de la prueba")
        self.label63.pack()
        self.label63.place(x="780", y="10")
        self.label73 = tkinter.Label(self.page1, text="     ...")
        self.label73.pack()
        self.label73.place(x="780", y="40")

        self.boton13 = tkinter.Button(self.page3, text="Iniciar", command=self.controlador.agregar_datosTree3, width=15, height=5)
        self.boton13.pack()
        self.boton13.place(x="760", y="150")

        self.boton23 = tkinter.Button(self.page3, text="Generar Graficas ", command=self.controlador.abrir_graficasPestaña3, width=15, height=5)
        self.boton23.pack()
        self.boton23.place(x="760", y="270")

        self.boton33 = tkinter.Button(self.page3, text="Parar Prueba", command="", width=15, height=5)
        self.boton33.pack()
        self.boton33.place(x="760", y="390")

        self.tree3 = ttk.Treeview(self.page3, height=20)
        self.tree3['columns'] = ('Columna1', 'Columna2', 'Columna3')

        self.tree3.heading('#0', text='Índice')
        self.tree3.column('#0', anchor=tkinter.CENTER, width=80)
        self.tree3.heading('Columna1', text='Fuerza Horizontal')
        self.tree3.column('Columna1', anchor=tkinter.CENTER, width=170)
        self.tree3.heading('Columna2', text='Desplazamiento Horizontal')
        self.tree3.column('Columna2', anchor=tkinter.CENTER, width=170)
        self.tree3.heading('Columna3', text='Desplazamiento Vertical')
        self.tree3.column('Columna3', anchor=tkinter.CENTER, width=170)
        self.tree3.pack()
        self.tree3.place(x=80, y=100)

        #------------------------------------------------------------------
    def agregar_datosTree3(self, datos):
        for fila in self.tree3.get_children():
            self.tree3.delete(fila)
        for indice, fila in enumerate(datos):
            valores = fila
            self.tree3.insert('', 'end', text=str(indice), values=valores)

    def agregar_datosTree2(self, datos):
        for fila in self.tree2.get_children():
            self.tree2.delete(fila)
        for indice, fila in enumerate(datos):
            valores = fila
            self.tree2.insert('', 'end', text=str(indice), values=valores)

    def agregar_datosTree1(self, datos):
        for fila in self.tree1.get_children():
            self.tree1.delete(fila)
        for indice, fila in enumerate(datos):
            valores = fila
            self.tree1.insert('', 'end', text=str(indice), values=valores)

    def cerrar_pestaña(self):
        self.ventana3.destroy()

    def obtener_datosPage1(self):
        return (self.value_inside1.get(), self.entry11.get(), self.entry21.get(), self.entry41.get())

    def obtener_datosPage2(self):
        return (self.value_inside2.get(), self.entry12.get(), self.entry22.get(), self.entry42.get())

    def obtener_datosPage3(self):
        return (self.value_inside3.get(), self.entry13.get(), self.entry23.get(),self.entry43.get())

    def iniciar(self):
        self.ventana3.mainloop()