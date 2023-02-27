import tkinter as tk  # knihovna pro tvoření okna, tlačítek a pole
import keyboard # knihovna pro použití klávesnice
from tkinter import*
from Basic import *
from Function import *

"""
Window.py
Vkládáme soubory "Basic.py" a "Function.py", díky kterým, voláme potřebné funkce.
První knohivna "tkinter", která slouží vytvoření okna, pole a tlačítek.    
Druhá knihovna "keyboard", která slouží ke spouštění tlačítka skrze klávesnici.
"""
 
 
"""
První odstavec vytváří okno, díky dříve zmíněné knihovně "tkinter" a dále pole "field",
díky které vidíme, co jsme vložili do kalkulačky.
"""
 
# Window
# Tvoření samotného okna, "geometry" slouží k celkové velikost okna
# Dále tvoření field, neboli pole kde budeme vkládat čísla, znaménka a provádět výpočty
window = Tk()
window.geometry("400x250")
field = tk.Text(window, height= 2, width=21, font=("Times new roman", 20))
field.grid(row=1, column=1, columnspan=7)

"""
Druhý  odstavec vytváří opět díky "tkinter" veškerá tlačítka.
Tlačítka slouží k volání funkcí ze souborů "Basic.py" a "Function.py", k zapisování
čísel a základním znamének do pole, a také k výslednému počítání.
"""

# Button commands
# Zde tvoříme jednotlivá tlačítka, zároveň jim udaváme co mají v sobě napsané, font a hlavně jejich funkci
# Jednotlivá čísla
button_1 = tk.Button(window, text="1", command = lambda: add_to_field(1, field), width=3, font=("Times new roman", 15))
button_2 = tk.Button(window, text="2", command = lambda: add_to_field(2, field), width=3, font=("Times new roman", 15))
button_3 = tk.Button(window, text="3", command = lambda: add_to_field(3, field), width=3, font=("Times new roman", 15))
button_4 = tk.Button(window, text="4", command = lambda: add_to_field(4, field), width=3, font=("Times new roman", 15))
button_5 = tk.Button(window, text="5", command = lambda: add_to_field(5, field), width=3, font=("Times new roman", 15))
button_6 = tk.Button(window, text="6", command = lambda: add_to_field(6, field), width=3, font=("Times new roman", 15))
button_7 = tk.Button(window, text="7", command = lambda: add_to_field(7, field), width=3, font=("Times new roman", 15))
button_8 = tk.Button(window, text="8", command = lambda: add_to_field(8, field), width=3, font=("Times new roman", 15))
button_9 = tk.Button(window, text="9", command = lambda: add_to_field(9, field), width=3, font=("Times new roman", 15))
button_0 = tk.Button(window, text="0", command = lambda: add_to_field(0, field), width=3, font=("Times new roman", 15))

# Základní znaménka
button_plus = tk.Button(window, text="+", command = lambda: add_to_field("+", field), width=3, font=("Times new roman", 15))
button_minus = tk.Button(window, text="-", command = lambda: add_to_field("-", field), width=3, font=("Times new roman", 15))
button_krat = tk.Button(window, text="*", command = lambda: add_to_field( "*", field), width=3, font=("Times new roman", 15))
button_deleno = tk.Button(window, text="/", command = lambda: add_to_field( "/", field), width=3, font=("Times new roman", 15))

# Závorky a desetinna
button_lzavor = tk.Button(window, text="(", command=lambda: add_to_field("(", field), width=3, font=("Times new roman", 15))
button_pzavor = tk.Button(window, text=")", command=lambda: add_to_field(")", field), width=3, font=("Times new roman", 15))
button_desetinna = tk.Button(window, text=".", command = lambda: add_to_field(".", field), width=3, font=("Times new roman", 15))

# Pkročilé matmatické funkce
button_faktorial = tk.Button(window, text="!", command = lambda: faktorial(field), width=3, font=("Times new roman", 15))
button_odmocnina = tk.Button(window, text="√", command=lambda: odmocnina(field), width=3, font=("Times new roman", 15))
button_mocnina = tk.Button(window, text="x²", command=lambda: mocnina(field), width=3, font=("Times new roman", 15))

# Goniometrické funkce
button_sin = tk.Button(window, text="sin", command=lambda: sin(field), width=3, font=("Times new roman", 15))
button_cos = tk.Button(window, text="cos", command=lambda: cos(field), width=3, font=("Times new roman", 15))
button_tg = tk.Button(window, text="tg", command=lambda: tg(field), width=3, font=("Times new roman", 15))
button_cotg = tk.Button(window, text="cotg", command=lambda: cotg(field), width=3, font=("Times new roman", 15))

# Výpočet a čištění pole
button_clear = tk.Button(window, text="Clear", command=lambda: clear(field), width=7, font=("Times new roman", 15))
button_rovnase = tk.Button(window, text="=", command=lambda: calculate(field), width=7, font=("Times new roman", 15))

"""
Funkce grid nám slouží k umístění jednodtlivích tlačítek v okně.
"""

# Umístění jednotlivých tlačítek do okna
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

button_rovnase.grid(row = 7, column= 6, columnspan=2)
button_clear.grid(row = 7, column= 4, columnspan=2)
    
    
#################
### Key press ###
#################

# Zde požíváme funkci bind a knihovnu keyboard, abychom mohli použít klávesnici k použití naší kalkulačky

"""
V poslední části používáme funkci "bind" a knihovnu "keyboard", ty slouží k
používání klakulačky  pomocí klávesnice.
Objí slouží k volání přímo funkcí, nikoliv tlačítka.
"""

### Cisla ###
window.bind('1', lambda event: add_to_field(1, field))
window.bind('2', lambda event: add_to_field(2, field))
window.bind('3', lambda event: add_to_field(3, field))
window.bind('4', lambda event: add_to_field(4, field))
window.bind('5', lambda event: add_to_field(5, field))
window.bind('6', lambda event: add_to_field(6, field))
window.bind('7', lambda event: add_to_field(7, field))
window.bind('8', lambda event: add_to_field(8, field))
window.bind('9', lambda event: add_to_field(9, field))
window.bind('0', lambda event: add_to_field(0, field))

### Znaménka ###
window.bind('+', lambda event: add_to_field("+", field))
window.bind('-', lambda event: add_to_field("-", field))
window.bind('*', lambda event: add_to_field("*", field))
window.bind('/', lambda event: add_to_field("/", field))

### Funkce ###
window.bind(',', lambda event: add_to_field(".", field))
window.bind('.', lambda event: add_to_field(".", field))

keyboard.add_hotkey('Enter', lambda: calculate(field))
keyboard.add_hotkey('Backspace', lambda: clear(field))
keyboard.add_hotkey('Shift + §', lambda: faktorial(field))
keyboard.add_hotkey(')', lambda: add_to_field(")", field))
keyboard.add_hotkey('Shift + )', lambda: add_to_field("(", field))    
    
window.mainloop()
