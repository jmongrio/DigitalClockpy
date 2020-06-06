#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Import essential modules
from tkinter import *
from time import strftime

#Crear contenedor y titulo de ventana
root = Tk()
root.focus()
root.title("Reloj digital en python")

#Mostrar algún texto ficticio en la pantalla
myClock = Label()
myClock['text'] = '21:18:00'
myClock.pack()

#Cambio font
myClock['font'] = 'Ubuntu 150 bold'

#Obtener tiempo del sistema
strftime('%H:%M:%S')

#Funciones que manipuen el tiempo
def tic():
    myClock['text'] = strftime('%H:%M:%S')

tic()

def tac():
    tic()
    myClock.after(1000,tac)

tac()

root.mainloop()
