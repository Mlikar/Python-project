
# Projekt kalkulačky v Pythonu

import tkinter as tk
from tkinter import *
import math
import keyboard



field_text=""
nahrada = 0

# Window = zde tvoříme základní okno a velikost pole

window = Tk()
window.geometry("400x250")
field = tk.Text(window, height= 2, width=21, font=("Times new roman", 20))
field.grid(row=1, column=1, columnspan=7)


# Základ

#vkládání čísel a znamének do pole
def add_to_field(add): 
    global field_text
    field_text = field_text+str(add)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)
   # nahrada = field_text

# funkce pro výpočet
def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
    field_text = result

 # funkce pro vyčištění pole
def clear():
    global field_text
    global nahrada
    field_text = ""
    nahrada = 0
    field.delete ("1.0", "end")

# Funkce
# zde používáme knihovnu math pro matematické úlohy
def odmocnina():
    global field_text
    sqrt = (math.sqrt(float(field_text)))
    field.delete("1.0", "end")
    field.insert("1.0", sqrt)
    field_text = str(sqrt)

def mocnina():
    global field_text
    pow = math.pow(float(field_text), 2)
    field.delete("1.0", "end")
    field.insert("1.0", pow)
    field_text = str(pow)

def faktorial():
    global field_text
    factorial = math.factorial(int(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", factorial)
    field_text = str(factorial)

def sin():
    global field_text
    sin = math.sin(float(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", sin)
    field_text = str(sin)

def cos():
    global field_text
    cos = math.cos(float(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", cos)
    field_text = str(cos)

def tg():
    global field_text
    tg = math.tan(float(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", tg)
    field_text = str(tg)

def cotg():
    global field_text
    cotg = math.cos(int(field_text)) / math.sin(int(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", cotg)
    field_text = str(cotg)


# tvoření tlačítek a jejich funkce
button_1 = tk.Button(window, text="1", command = lambda: add_to_field(1), width=3, font=("Times new roman", 15))
button_2 = tk.Button(window, text="2", command = lambda: add_to_field(2), width=3, font=("Times new roman", 15))
button_3 = tk.Button(window, text="3", command = lambda: add_to_field(3), width=3, font=("Times new roman", 15))
button_4 = tk.Button(window, text="4", command = lambda: add_to_field(4), width=3, font=("Times new roman", 15))
button_5 = tk.Button(window, text="5", command = lambda: add_to_field(5), width=3, font=("Times new roman", 15))
button_6 = tk.Button(window, text="6", command = lambda: add_to_field(6), width=3, font=("Times new roman", 15))
button_7 = tk.Button(window, text="7", command = lambda: add_to_field(7), width=3, font=("Times new roman", 15))
button_8 = tk.Button(window, text="8", command = lambda: add_to_field(8), width=3, font=("Times new roman", 15))
button_9 = tk.Button(window, text="9", command = lambda: add_to_field(9), width=3, font=("Times new roman", 15))
button_0 = tk.Button(window, text="0", command = lambda: add_to_field(0), width=3, font=("Times new roman", 15))

button_plus = tk.Button(window, text="+", command = lambda: add_to_field("+"), width=3, font=("Times new roman", 15))
button_minus = tk.Button(window, text="-", command = lambda: add_to_field("-"), width=3, font=("Times new roman", 15))
button_krat = tk.Button(window, text="*", command = lambda: add_to_field("*"), width=3, font=("Times new roman", 15))
button_deleno = tk.Button(window, text="/", command = lambda: add_to_field("/"), width=3, font=("Times new roman", 15))

button_lzavor = tk.Button(window, text="(", command = lambda: add_to_field("("), width=3, font=("Times new roman", 15))
button_pzavor = tk.Button(window, text=")", command = lambda: add_to_field(")"), width=3, font=("Times new roman", 15))
button_desetinna = tk.Button(window, text=".", command = lambda: add_to_field("."), width=3, font=("Times new roman", 15))

button_faktorial = tk.Button(window, text="!", command = lambda: faktorial(), width=3, font=("Times new roman", 15))
button_mocnina = tk.Button(window, text="x²", command = lambda: mocnina(), width=3, font=("Times new roman", 15))
button_odmocnina = tk.Button(window, text="²√", command = lambda: odmocnina(), width=3, font=("Times new roman", 15))

button_sin = tk.Button(window, text="sin", command = lambda: sin(), width=3, font=("Times new roman", 15))
button_cos = tk.Button(window, text="cos", command = lambda: cos(), width=3, font=("Times new roman", 15))
button_tg = tk.Button(window, text="tg", command = lambda: tg(), width=3, font=("Times new roman", 15))
button_cotg = tk.Button(window, text="cotg", command = lambda: cotg(), width=3, font=("Times new roman", 15))

button_clear = tk.Button(window, text="Clear", command = lambda: clear(), width=7, font=("Times new roman", 15))
button_rovna_se = tk.Button(window, text="=", command = lambda: calculate(), width=7, font=("Times new roman", 15))

# umístění jednotlivých tlačítek do okna
button_1.grid(row = 4, column= 1)
button_2.grid(row = 4, column= 2)
button_3.grid(row = 4, column= 3)
button_4.grid(row = 5, column= 1)
button_5.grid(row = 5, column= 2)
button_6.grid(row = 5, column= 3)
button_7.grid(row = 6, column= 1)
button_8.grid(row = 6, column= 2)
button_9.grid(row = 6, column= 3)
button_0.grid(row = 7, column= 2)

button_plus.grid(row = 4, column= 4)
button_minus.grid(row = 4, column= 5)
button_krat.grid(row = 5, column= 4)
button_deleno.grid(row = 5, column= 5)

button_lzavor.grid(row = 6, column= 4)
button_pzavor.grid(row = 6, column= 5)
button_desetinna.grid(row = 7, column= 1)

button_faktorial.grid(row = 7, column= 3)
button_mocnina.grid(row = 6, column= 6)
button_odmocnina.grid(row =6, column= 7)

button_sin.grid(row = 4, column= 6)
button_cos.grid(row = 4, column= 7)
button_tg.grid(row = 5, column= 6)
button_cotg.grid(row = 5, column= 7)

button_rovna_se.grid(row = 7, column= 6, columnspan=2)
button_clear.grid(row = 7, column= 4, columnspan=2)

#################
### Key press ###
#################

# funkce bind a knihovna keyboard, pro počítání pomocí klávesnice
### Cisla ###
window.bind('1', lambda event: add_to_field(1))
window.bind('2', lambda event: add_to_field(2))
window.bind('3', lambda event: add_to_field(3))
window.bind('4', lambda event: add_to_field(4))
window.bind('5', lambda event: add_to_field(5))
window.bind('6', lambda event: add_to_field(6))
window.bind('7', lambda event: add_to_field(7))
window.bind('8', lambda event: add_to_field(8))
window.bind('9', lambda event: add_to_field(9))
window.bind('0', lambda event: add_to_field(0))

### Znaménka ###
window.bind('+', lambda event: add_to_field("+"))
window.bind('-', lambda event: add_to_field("-"))
window.bind('*', lambda event: add_to_field("*"))
window.bind('/', lambda event: add_to_field("/"))

### Funkce ###
window.bind(',', lambda event: add_to_field("."))
window.bind('.', lambda event: add_to_field("."))

keyboard.add_hotkey('Enter', lambda: calculate())
keyboard.add_hotkey('Backspace', lambda: clear())
keyboard.add_hotkey('Shift + §', lambda: faktorial())
keyboard.add_hotkey(')', lambda: add_to_field(")"))
keyboard.add_hotkey('Shift + )', lambda: add_to_field("("))


window.mainloop() 



