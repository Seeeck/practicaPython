
#Funcion recursica sin retorno
def cuenta_atras(num):
    num -= 1
    if num > 0:
     print(num)
     cuenta_atras(num)
    else:
     print("Boooooooom!")
    print("Fin de la función", num)


cuenta_atras(5)

#Funcion recursiva con retorno
def factorial(num):
    print("Valor inicial ->", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("valor final ->", num)
    return num


print(factorial(5))
 
