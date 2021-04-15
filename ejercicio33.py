def leer_numero(ini,fin,mensaje):
    while True:
        numero=int(input(mensaje))
        if numero<ini or numero>fin:
            return numero
            break
            
def generador():
    numeros=leer_numero(1, 20, '¿Cuantos números quieres generar? [1-20]')
    modo=leer_numero(1, 3, '¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal')

    