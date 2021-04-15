texto = ("un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro")

""" texto=texto.replace('#','\n - ') """
texto = texto.split('#')
cadena = ""
for i in texto:
    if texto.index(i) == 0:
        i = i.capitalize()
        cadena = cadena+i+'... \n - '
    elif texto.index(i) != 3:
        i = i.capitalize()
        cadena = cadena+i+'.\n - '
    elif texto.index(i) == 3:
        i = i.capitalize()
        cadena = cadena+i+'.'


print(cadena)
