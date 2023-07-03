import tkinter as tk
from tkinter import Frame, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Vista_Pestaña1:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventanaP1 = tk.Tk()
        self.ventanaP1.title("Datos Generales")
        self.ventanaP1.geometry("1200x700")
        self.ventanaP1.resizable(False, False)

        self.main_frame = tk.Frame(self.ventanaP1)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.create_treeview()
        self.create_plot()
        self.label1 = tk.Label(self.left_frame, text="Nombre del archivo")
        self.label1.pack()
        self.entry1 = tk.Entry(self.left_frame)
        self.entry1.pack()
        self.crear_boton()
    def agregar_datosarbolpestaña1(self, datos):
        for fila in self.tree1.get_children():
            self.tree1.delete(fila)
        for indice, fila in enumerate(datos):
            valores = fila
            self.tree1.insert('', 'end', text=str(indice), values=valores)
    def create_treeview(self):
        self.tree1 = ttk.Treeview(self.right_frame, height=20)
        self.tree1['columns'] = ('Columna1', 'Columna2', 'Columna3','Columna4')

        self.tree1.heading('#0', text='Índice')
        self.tree1.column('#0', anchor=tk.CENTER, width=80)
        self.tree1.heading('Columna1', text='Fuerza Horizontal \n N')
        self.tree1.column('Columna1', anchor=tk.CENTER, width=100)
        self.tree1.heading('Columna2', text='Desplazamiento Horizontal \n mm')
        self.tree1.column('Columna2', anchor=tk.CENTER, width=100)
        self.tree1.heading('Columna3', text='Desplazamiento Vertical \n mm')
        self.tree1.column('Columna3', anchor=tk.CENTER, width=100)
        self.tree1.heading('Columna4', text='Esfuerzo cortante')
        self.tree1.column('Columna4', anchor=tk.CENTER, width=100)
        self.tree1.pack(side=tk.LEFT, padx=10, pady=10)

    def create_plot(self):
        fig1 = Figure(figsize=(5, 4), dpi=100)
        ax1 = fig1.add_subplot(111)
        x = [0, 0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4]
        y = [0, 3.514132926, 5.551311434, 6.977336389, 7.894066718, 8.148714031, 8.148714031, 8.148714031, 8.148714031,
             8.148714031, 8.148714031]
        ax1.scatter(x, y)
        ax1.plot(x, y, 'r-')  # 'r-' indica una línea roja

        canvas = FigureCanvasTkAgg(fig1, master=self.left_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=10, pady=10)
    def crear_boton(self):
        self.boton = tk.Button(self.left_frame, text="Generar Graficas", command=self.controlador.generar_pdf,
                                   width=25, height=5, borderwidth=2)
        self.boton.pack()
    def obtener_nombreArchivo(self):
        return self.entry1.get()
    def cerrar_pestaña(self):
        self.ventanaP1.destroy()
    def iniciar(self):
        self.ventanaP1.mainloop()