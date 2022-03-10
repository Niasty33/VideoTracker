import tkinter as tk
import PIL.Image, PIL.ImageTk

class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.menu_bar = tk.Canvas(bg="magenta", width=50, height=550)
        self.menu_bar.grid(row=0, column=0, rowspan=3)

        self.page = tk.Canvas(bg="white", width=900, height=500)
        self.page.grid(row=0, column=1, rowspan=2)

        self.gestion = tk.Canvas(bg="black", width=900, height=50)
        self.gestion.grid(row=2, column=1)

        self.convert_csv_btn = tk.Button(self.parent, text="Convert to csv", width=10)
        self.convert_csv_btn.grid(row=0, column=3, padx=5, pady=5)
        
    
    def setController(self, controller):
        self.controller = controller

    