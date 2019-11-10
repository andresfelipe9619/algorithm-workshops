from tkinter import *
from random import randint

""" 2DO PUNTO"""
def numberGenerator():
    """
    numero_inicio: entero
    numero_fin: entero
    numero_random: entero

    x = ingresa 1er numero
    y = ingresa 2do numero
    si x > y numero_inicio = y y numero_fin=x
    de lo contrario si y > x numero_inicio = x y numero_fin=y

    numero_random = hacer randorm de numero_inicio a numero_fin

    mostar numero_random
    """
    
    x = int(SNumero1.get())
    y = int(SNumero2.get())
    if x<y:
         mRandom = int(randint(x,y))
    elif x>y:
         mRandom = int(randint(y,x))
 
    EGenerado.config(state=NORMAL)
    EGenerado.delete(0, END)
    EGenerado.insert(0, mRandom)
    EGenerado.config(state=DISABLED)



gui = Tk()

gui.geometry("300x200")

LNumero1 = Label(gui, text="Numero 1")
LNumero2 = Label(gui, text="Numero 2")
LGenerado = Label(gui, text="Numero Generado")
EGenerado = Entry(gui, width=30)
EGenerado.config(state=DISABLED)


SNumero1 = Spinbox(gui, from_=0, to=1000)
SNumero2 = Spinbox(gui, from_=0, to=1000)

BGenerar = Button(gui, text="Generar", command=numberGenerator)


LNumero1.pack()
SNumero1.pack()
LNumero2.pack()
SNumero2.pack()
LGenerado.pack()
EGenerado.pack()
BGenerar.pack()
gui.mainloop()