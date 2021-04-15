numeros = [1, 3, 6, 9]



while True:
    num=(int(input("Ingrese un numero del 0 al 9:")))
    if num>0 and num<10:
        for i in numeros:
            if num==i:
                print("el numero ya existe")
    else:
        continue
     
   

    


