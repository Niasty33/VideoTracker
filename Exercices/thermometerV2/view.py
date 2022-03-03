from tkinter import *

class View(Frame):

    def __init__(self, parent):

        super().__init__(parent)
        self.parent = parent

        self.celsius_btn = Button(self.parent, text ='Celsius', width = 10)
        self.celsius_btn.grid(row=0, column=0, padx=5, pady=5)
        
        self.fahrenheit_btn = Button(self.parent, text ='Fahrenheit', width = 10)
        self.fahrenheit_btn.grid(row=0, column=1, padx=5, pady=5)

        self.kelvin_btn = Button(self.parent, text = 'Kelvin', width = 10)
        self.kelvin_btn.grid(row=0, column=2, padx=5, pady=5)

        self.temperature_lbl = Label(self.parent, width='20', height = '5', font = ('Arial', 25), bg='ivory')
        self.temperature_lbl.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.increase_btn = Button(self.parent, text ='Increase')
        self.increase_btn.grid(row=2, column=2, padx=5, pady=5)

        self.decrease_btn = Button(self.parent, text ='Decrease')
        self.decrease_btn.grid(row=2, column=0, padx=5, pady=5)
        

    def update(self, text : str) -> None:
        
        self.temperature_lbl.config(text = text)