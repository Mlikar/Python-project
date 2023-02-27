
"""
Basic.py
Zde se náchází první tři základní funkce naší kalkulačky a základní proměnná, která slouží k
zapisování do pole(field).
"""

field_text=""  # Proměná do které, vkládáme čísla a znaménka, které chceme v poli

"""
Funkce add_to_field
Zapisuje do pole číslo nebo základní znaménko.
"""

# Tato funkce slouží k přidávání čísel a znamének do pole (field)
def add_to_field(add, field):
    global field_text
    field_text = field_text+str(add)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

"""
Funkce calculate
Vezme čísla a základní znaménka z pole, vloží je do proměnné "result" a výsledek zobrazí v poli
Pak proměnnou "result", vkládáme do proměnné "field_text," abychom mohli s výsledkem dále počítat.
"""

# Funkce pro finální výpočet příkladu
# Proměná result slouží k tomu, abychom pak s výsledkem mohli počítat dále 
def calculate(field):
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
    field_text = result

"""
Funkce clear
Tato funkce vyčistí pole a vymaže data z proměnných.
""" 
    
 # Funkce pro vyčištění pole a proměných
def clear(field):
    global field_text
    global nahrada
    field_text=""
    nahrada = 0
    field.delete ("1.0", "end")
