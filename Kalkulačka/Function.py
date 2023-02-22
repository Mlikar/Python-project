
import math
import Basic

# Funkce
# Zde používáme knihovnu math pro matematické úlohy
# Tyto funkce fungují podobně jako funkce calculate, při použit vyhodí rovnou výsledek, avšak počítají pouze s jedním číslem

# Funkce pro odmocninu 
def odmocnina(field):
    sqrt = math.sqrt(float(Basic.field_text))
    field.delete("1.0", "end")
    field.insert("1.0", sqrt)
    field_text = str(sqrt)

# Funkce pro mocninu
def mocnina(field):
    pow = math.pow(float(Basic.field_text), 2)
    field.delete("1.0", "end")
    field.insert("1.0", pow)
    field_text = str(pow)

# Funkce pro faktorial
def faktorial(field):
    factorial = math.factorial(int(Basic.field_text))
    field.delete("1.0", "end")
    field.insert("1.0", factorial)
    field_text = str(factorial)

# Funkce pro sinus
def sin(field):
    sin = math.sin(float(Basic.field_text))
    field.delete("1.0", "end")
    field.insert("1.0", sin)
    field_text = str(sin)

# Funkce pro cosinus
def cos(field):
    cos = math.cos(float(Basic.field_text))
    field.delete("1.0", "end")
    field.insert("1.0", cos)
    field_text = str(cos)

# Funkce pro tangenc
def tg(field):
    tg = math.tan(float(Basic.field_text))
    field.delete("1.0", "end")
    field.insert("1.0", tg)
    field_text = str(tg)

# Funkce pro cotangenc
def cotg(field):
    cotg = math.cos(int(Basic.field_text)) / math.sin(int(Basic.field_text))
    field.delete("1.0", "end")
    field.insert("1.0", cotg)
    field_text = str(cotg)
