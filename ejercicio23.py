numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(lista):
    pares=[]
    impares=[]
    for i in numeros:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
    print(pares)
    print(impares)


separar(numeros)