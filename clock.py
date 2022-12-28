#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Import essential modules
from tkinter import *
from time import strftime

#Crear contenedor y titulo de ventana
root = Tk()
root.focus()
root.resizable(0, 0)
root.title("Digital Clock")
root.iconbitmap("favicon.ico")
root.config(bg='#fff')

#Mostrar algún texto ficticio en la pantalla
myClock = Label(root, background='#fff', foreground="#808080")
myClock['text'] = 'XX:XX:XX'
myClock.grid(row=0, column=0)

name = Label(root, background='#fff', foreground="#808080")
name['text'] = 'By Jasón Mongrillo'
name.place(relx = 1.0, rely = 0.0, anchor='se')
name.grid(row=1, column=0, sticky='e')

#Cambio font
myClock['font'] = 'Verdana 150 bold'
name['font'] = 'Verdana 12'

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
