import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


class Vista_Pestaña1:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventanaP1 = tk.Tk()
        self.ventanaP1.title("Datos Generales")
        self.ventanaP1.geometry("900x600")
        self.ventanaP1.resizable(False, False)
        self.canvas = tk.Canvas(self.ventanaP1)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame = tk.Frame(self.canvas)

        self.vsb = tk.Scrollbar(self.ventanaP1, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.bind("<Enter>", self.bind_mousewheel)
        self.canvas.bind("<Leave>", self.unbind_mousewheel)
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)

        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)

        self.fig1 = Figure(figsize=(5, 4), dpi=100)
        self.ax1 = self.fig1.add_subplot(111)
        self.x = [1, 2, 3, 4, 5]
        self.y = [2, 4, 6, 8, 10]
        self.ax1.plot(self.x, self.y)
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.frame)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack()

        self.fig2 = Figure(figsize=(5, 4), dpi=100)
        self.ax2 = self.fig2.add_subplot(111)
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        y = np.sin(x)
        self.ax2.fill_between(x, y, where=(y < 0), color='red', alpha=0.5)
        self.ax2.fill_between(x, y, where=(y >= 0), color='blue', alpha=0.5)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.frame)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack()

        self.fig1 = Figure(figsize=(5, 4), dpi=100)
        self.ax1 = self.fig1.add_subplot(111)
        self.x = [1, 2, 3, 4, 5]
        self.y = [2, 4, 6, 8, 10]
        self.ax1.plot(self.x, self.y)
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.frame)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))

    def bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self.mousewheel)

    def unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def iniciar(self):
        self.ventanaP1.mainloop()