def suma(operando1,operando2):
    resultado = operando1+operando2

    return resultado

def division(operando1,operando2):
    resultado = operando1/operando2

    return resultado
#Iniciando el programa Principal 

opc = 0

while opc != 5:
    print("----------------------Calculadora para el Stream GIT/GITHUB----------------------\n\n")
    print("Eliga una opcion de las siguientes:\n")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Division")
    print("4.- Multiplicación")
    print("5.- Salir\n")

    opc = int(input("Selecciona su opcion: "))
    if opc == 1:
        op1 = int(input("Ingrese el primero operando: "))
        op2 = int(input("Ingrese el segundo operando: "))
        print("Rellizando la suma:\n")
        print(suma(op1,op2))

    elif opc == 2:
        op1 = int(input("Ingrese el primero operando: "))
        op2 = int(input("Ingrese el segundo operando: "))
        print("Rellizando la Resta:\n")
    elif opc == 3:
        op1 = int(input("Ingrese el primero operando: "))
        op2 = int(input("Ingrese el segundo operando: "))
        print("Rellizando la División:\n")
    elif opc == 4:
        op1 = int(input("Ingrese el primero operando: "))
        op2 = int(input("Ingrese el segundo operando: "))
        print("Rellizando la Multiplicacion:\n")
    elif opc == 5:
        print("Saliendo...\n")
    else:
        print("Opción incorrecta\n")


print("Finalizando programa...")