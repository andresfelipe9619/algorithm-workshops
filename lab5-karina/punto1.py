from tkinter import *

""" 1ER PUNTO"""
def tomaTemperatura():
   temp =  int(ETemperatura.get())
   return temp

def farenheitKelvin():
    """
    farenheit: entero
    kelvin : entero

    farenheit = tomaTemeperatura
    kelvin = (5*(farenheit - 32)/9) + 273

    mostrar kelvin

    """
    farenheit = tomaTemperatura()
    kelvin = (5*(farenheit - 32)/9) + 273
    EResultado.delete(0, END)
    EResultado.insert(0, kelvin)
    
def celciusFarenheit():
    """
    farenheit: entero
    celcius : entero

    celcius = tomaTemeperatura
    farenheit = (9 * celcius / 5)+32

    mostrar celcius

    """
    celcius = tomaTemperatura()
    farenheit = (9 * celcius / 5)+32
    EResultado.delete(0, END)
    EResultado.insert(0, farenheit)

def celciusKelvin():
    """
    celcius: entero
    kelvin : entero

    celcius = tomaTemeperatura
    kelvin = celcius + 273

    mostrar kelvin
    """ 
    celcius = tomaTemperatura()
    kelvin = celcius + 273
    EResultado.delete(0, END)
    EResultado.insert(0, kelvin)

def kelvinFarenheit():
    """
    farenheit: entero
    kelvin : entero

    farenheit = tomaTemeperatura
    kelvin = farenheit + 273

    mostrar kelvin
    """
    kelvin = tomaTemperatura()
    farenheit = (9*(kelvin - 273)/5) + 32
    EResultado.delete(0, END)
    EResultado.insert(0, farenheit)

def kelvinCelcius():
    """
    celcius: entero
    kelvin : entero

    kelvin = tomaTemeperatura
    celcius = kelvin - 273

    mostrar kelvin
    """
    kelvin = tomaTemperatura()
    celcius = kelvin - 273
    EResultado.delete(0, END)
    EResultado.insert(0, celcius)

def farenheitCelcius():
    """
    celcius: entero
    farenheit : entero

    farenheit = tomaTemeperatura
    celcius = 5 * (farenheit - 32) / 9

    mostrar celcius
    """
    farenheit = tomaTemperatura()
    celcius = 5 * (farenheit - 32) / 9
    EResultado.delete(0, END)
    EResultado.insert(0, celcius)
    


gui = Tk()
gui.geometry("400x300")

LTemperatura=Label(gui, text = "Igrese la temperatura")
ETemperatura = Entry(gui, width = 20)

"""BOTONES"""
BFarenheitCelcius = Button(gui, text="Farenheit a Celcius", command=farenheitCelcius, width=15)
BCelciusFarenheit = Button(gui, text="Celcius a Farenheit", command=celciusFarenheit, width=15)
BKelvinCelcius = Button(gui, text="Kelvin a Celcius", command=kelvinCelcius, width=15)
BCelciusKelvin = Button(gui, text="Celcius a Kelvin", command=celciusKelvin, width=15)
BFarenheitKelvin = Button(gui, text="Farenheit a Kelvin", command=farenheitKelvin, width=15)
BKelvinFarenheit = Button(gui, text="Kelvin a Farenheit", command=kelvinFarenheit, width=15)

"""RESULTADO"""
LResultado = Label(gui, text="Resultado")
EResultado = Entry(gui, width=20)

LTemperatura.place(x=80, y=20)
ETemperatura.place(x=200, y=20)
BFarenheitCelcius.place(x=80, y=70)
BCelciusFarenheit.place(x=200, y=70)
BKelvinCelcius.place(x=80, y=120)
BCelciusKelvin.place(x=200, y=120)
BFarenheitKelvin.place(x=80, y=170)
BKelvinFarenheit.place(x=200, y=170)


LResultado.place(x=150, y=220)
EResultado.place(x=130, y=250)
gui.mainloop()


