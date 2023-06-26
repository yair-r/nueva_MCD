import tkinter as tkinter
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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

        self.label21 = tkinter.Label(self.page1, text="Dimenciones del molde (caja-area | cilindro-radio)")
        self.label21.pack()
        self.label21.place(x="170", y="10")
        self.entry11 = tkinter.Entry(self.page1)
        self.entry11.pack()
        self.entry11.place(x="170", y="30")
        self.label31 = tkinter.Label(self.page1, text="velocidad de corte MM/min")
        self.label31.pack()
        self.label31.place(x="460", y="10")
        self.entry21 = tkinter.Entry(self.page1)
        self.entry21.pack()
        self.entry21.place(x="460", y="30")

        self.label51 = tkinter.Label(self.page1, text="Tencion vertical ")
        self.label51.pack()
        self.label51.place(x="630", y="10")
        self.entry41 = tkinter.Entry(self.page1)
        self.entry41.pack()
        self.entry41.place(x="630", y="30")

        self.label61 = tkinter.Label(self.page1, text="Nombre clave \n de la prueba")
        self.label61.pack()
        self.label61.place(x="780", y="10")

        self.boton11 = tkinter.Button(self.page1, text="Ver graficas", command="", width=15, height=5)
        self.boton11.pack()
        self.boton11.place(x="760", y="150")

        self.boton21 = tkinter.Button(self.page1, text="Ver siguiente prueba", command="", width=15, height=5)
        self.boton21.pack()
        self.boton21.place(x="760", y="270")

        self.boton31 = tkinter.Button(self.page1, text="Guardar en Base de datos", command="", width=15, height=5)
        self.boton31.pack()
        self.boton31.place(x="760", y="390")

        self.fig1 = Figure(figsize=(5, 4), dpi=100)
        self.ax1 = self.fig1.add_subplot(111)

        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.page1)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack()
        self.canvas1.get_tk_widget().configure(width=700, height=450)
        self.canvas1.get_tk_widget().place(x=20, y=100)

        # ----------------------------------------------------------------------

        self.label12 = tkinter.Label(self.page2, text="Forma del molde de corte")
        self.label12.pack()
        self.label12.place(x="15", y="10")
        self.options_list2 = ["Cuadrado", "Cilindro"]
        self.value_inside2 = tkinter.StringVar(self.page2)
        self.value_inside2.set("Molde")
        self.question_menu2 = tkinter.OptionMenu(self.page2, self.value_inside2, *self.options_list2)
        self.question_menu2.pack()
        self.question_menu2.place(x="15", y="30")

        self.label22 = tkinter.Label(self.page2, text="Dimenciones del molde (caja-area | cilindro-radio)")
        self.label22.pack()
        self.label22.place(x="170", y="10")
        self.entry12 = tkinter.Entry(self.page2)
        self.entry12.pack()
        self.entry12.place(x="170", y="30")

        self.label32 = tkinter.Label(self.page2, text="velocidad de corte MM/min")
        self.label32.pack()
        self.label32.place(x="460", y="10")
        self.entry22 = tkinter.Entry(self.page2)
        self.entry22.pack()
        self.entry22.place(x="460", y="30")

        self.label52 = tkinter.Label(self.page2, text="Tencion vertical ")
        self.label52.pack()
        self.label52.place(x="630", y="10")
        self.entry42 = tkinter.Entry(self.page2)
        self.entry42.pack()
        self.entry42.place(x="630", y="30")

        self.label62 = tkinter.Label(self.page2, text="Nombre clave \n de la prueba")
        self.label62.pack()
        self.label62.place(x="780", y="10")

        self.boton12 = tkinter.Button(self.page2, text="Ver graficas", command="", width=15, height=5)
        self.boton12.pack()
        self.boton12.place(x="760", y="150")

        self.boton22 = tkinter.Button(self.page2, text="Ver siguiente prueba", command="", width=15, height=5)
        self.boton22.pack()
        self.boton22.place(x="760", y="270")

        self.boton32 = tkinter.Button(self.page2, text="Guardar en Base de datos", command="", width=15, height=5)
        self.boton32.pack()
        self.boton32.place(x="760", y="390")

        self.fig2 = Figure(figsize=(5, 4), dpi=100)
        self.ax2 = self.fig2.add_subplot(111)

        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.page2)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack()
        self.canvas2.get_tk_widget().configure(width=700, height=450)
        self.canvas2.get_tk_widget().place(x=20, y=100)

        # ----------------------------------------------------------------------

        self.label13 = tkinter.Label(self.page3, text="Forma del molde de corte")
        self.label13.pack()
        self.label13.place(x="15", y="10")
        self.options_list3 = ["Cuadrado", "Cilindro"]
        self.value_inside3 = tkinter.StringVar(self.page3)
        self.value_inside3.set("Molde")
        self.question_menu3 = tkinter.OptionMenu(self.page3, self.value_inside3, *self.options_list3)
        self.question_menu3.pack()
        self.question_menu3.place(x="15", y="30")

        self.label23 = tkinter.Label(self.page3, text="Dimenciones del molde (caja-area | cilindro-radio)")
        self.label23.pack()
        self.label23.place(x="170", y="10")
        self.entry13 = tkinter.Entry(self.page3)
        self.entry13.pack()
        self.entry13.place(x="170", y="30")
        self.label33 = tkinter.Label(self.page3, text="velocidad de corte MM/min")
        self.label33.pack()
        self.label33.place(x="460", y="10")
        self.entry23 = tkinter.Entry(self.page3)
        self.entry23.pack()
        self.entry23.place(x="460", y="30")

        self.label53 = tkinter.Label(self.page3, text="Tencion vertical ")
        self.label53.pack()
        self.label53.place(x="630", y="10")
        self.entry43 = tkinter.Entry(self.page3)
        self.entry43.pack()
        self.entry43.place(x="630", y="30")

        self.label63 = tkinter.Label(self.page3, text="Nombre clave \n de la prueba")
        self.label63.pack()
        self.label63.place(x="780", y="10")

        self.boton13 = tkinter.Button(self.page3, text="Ver graficas", command="", width=15, height=5)
        self.boton13.pack()
        self.boton13.place(x="760", y="150")

        self.boton23 = tkinter.Button(self.page3, text="Ver siguiente prueba", command="", width=15, height=5)
        self.boton23.pack()
        self.boton23.place(x="760", y="270")

        self.boton33 = tkinter.Button(self.page3, text="Guardar en Base de datos", command="", width=15, height=5)
        self.boton33.pack()
        self.boton33.place(x="760", y="390")

        self.fig3 = Figure(figsize=(5, 4), dpi=100)
        self.ax3 = self.fig3.add_subplot(111)

        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.page3)
        self.canvas3.draw()
        self.canvas3.get_tk_widget().pack()
        self.canvas3.get_tk_widget().configure(width=700, height=450)
        self.canvas3.get_tk_widget().place(x=20, y=100)

    def obtener_datosPage1(self):
        return (self.value_inside1.get(), self.entry11.get(), self.entry21.get(), self.entry41.get())

    def obtener_datosPage2(self):
        return (self.value_inside2.get(), self.entry12.get(), self.entry22.get(), self.entry42.get())

    def obtener_datosPage3(self):
        return (self.value_inside3.get(), self.entry13.get(), self.entry23.get(),self.entry43.get())

    def iniciar(self):
        self.ventana3.mainloop()
