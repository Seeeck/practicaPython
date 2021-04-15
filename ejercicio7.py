from os import system as sys
import msvcrt
while(True):
    print('Programa de sumas')
    num1=int(input('Ingrese el primer numero:'))
    num2=int(input('Ingrese el segundo numero:'))
    print('Que quieres hacer?')
    print('1.Sumar los 2 numeros')
    print('2.Restar los 2 numeros')
    print('3.Multiplicar los 2 numeros')
    num=(int(input('Elige un numero:')))
    if(num==1):
        print('La suma da:',num1+num2)
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        sys('cls')
    elif(num==2):
        print('La resta da:',num1-num2)
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        sys('cls')
    elif(num==3):
        print('La multiplicacion da',num1*num2)
        print("Presione una tecla para continuar...")
        msvcrt.getch()
        sys('cls')
    else:
        print('Opcion invalida')

    
