
import tkinter as tk

field_text=""

def add_to_field(add, field):
    global field_text
    field_text = field_text+str(add)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)
   # nahrada = field_text

# funkce pro výpočet
def calculate(field):
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
    field_text = result

 # funkce pro vyčištění pole
def clear(field):
    global field_text
    global nahrada
    field_text=""
    nahrada = 0
    field.delete ("1.0", "end")