from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(weight.get())/float(height.get())/float(height.get())
        if value<16:            
            text.set(str('Выраженный дефицит массы тела'))
        elif value<18.5:
            text.set(str('Недостаточная (дефицит) масса тела'))
        elif value<25:
            text.set(str('Норма')
        elif value<30:
            text.set(str('Избыточная масса тела (предожирение)')
        elif value<35:
            text.set(str('Ожирение 1 степени')
        elif value<40:
            text.set(str('Ожирение 2 степени')
        else:
            text.set(str('Ожирение 3 степени')
    except ValueError:
        pass

