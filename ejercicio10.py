num=int(input("ingrese la cantidad de numeros:"))
suma=0
for i in range(num):
    suma+=float(input("Ingrese un numero"))
print("se han ingresado",num," numeros que dan un total de ",suma," y una media de ",suma/num)

