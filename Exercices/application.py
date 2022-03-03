from tkinter import *

class Application():

    def __init__(self):

        self.fenetre = Tk()
        self.fenetre.title("My thermometer")
        self.label = Label(self.fenetre, text="10°C", width='20', height = '5', font = ('Arial', 25), bg='ivory')
        self.label.pack(side=TOP, padx=5, pady=5)

        Button(self.fenetre, text ='Increase', command = self.increase).pack(side=LEFT, padx=5, pady=5)
        
        self.fenetre.mainloop()

    def increase(self):
        value = int(self.label['text'][:-2])
        unit = self.label['text'][-2:]
        self.label.config( text = str( value + 1 ) + unit)

if __name__ == '__main__':
    app = Application()