elementos = [1, 5, -2]

def agregar_una_vez(lista, el):
    
    try:
        if el in lista:
           raise ValueError("Error! No se permite un valor repetido")
        else:
           lista.append(el)
    except ValueError:
        print("Error! No se permite un valor repetido")
    

agregar_una_vez(elementos,-2)