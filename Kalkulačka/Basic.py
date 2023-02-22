
import tkinter as tk 

field_text=""  # proměná do které, vkládáme čísla a znaménka, které chceme v poli

# tato funkce slouží k přidávání čísel a znamének do pole (field)
def add_to_field(add, field):
    global field_text
    field_text = field_text+str(add)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)


# funkce pro finální výpočet příkladu
# proměná result slouží k tomu, abychom pak s výsledkem mohli počítat dále 
def calculate(field):
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
    field_text = result

 # funkce pro vyčištění pole a proměných
def clear(field):
    global field_text
    global nahrada
    field_text=""
    nahrada = 0
    field.delete ("1.0", "end")
