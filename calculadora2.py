while True:
    # entrada de numeros
    numero_1 = float(input("ingrese el primer numero: "))
    numero_2 = float(input("ingrese el segundo numero: "))
    # seleccion de opciones
    print(" >>> MENU <<< ")
    print(" >>> 1. SUMA ")
    print(" >>> 2. RESTA ")
    print(" >>> 3. MULTIPLICACION ")
    print(" >>> 4. DIVISION ")
    opcion = input(" Ingrese una opcion: \n")
    # calculo
    # suma
    if opcion == "1":
        suma = numero_1 + numero_2
        signo = "+"
        print(f" {numero_1} {signo} {numero_2} = {suma}")
    # resta
    elif opcion == "2":
        resta = numero_1 - numero_2
        signo = "-"
        print(f" {numero_1} {signo} {numero_2} = {resta}")
    # multiplicacion
    elif opcion == "3":
        multiplicacion = numero_1 * numero_2
        signo = "*"
        print(f" {numero_1} {signo} {numero_2} = {multiplicacion}")
    # division
    elif opcion == "4":
        division = numero_1 / numero_2
        signo = "*"
        print(f" {numero_1} {signo} {numero_2} = {division}")
    #distinto de las opciones    
    elif opcion != "1" and "2" and "3" and "4" :
        print("Elija una de las opciones")

    # salida de numeros(resultado)
    salir = input("\nPara salir ingrese 0 \nPara continuar ingrese cualquier tecla\n")
    if salir == "0":
        print("Calculadora finalizada")
        break
    elif salir != "0" :
        print("Continuamos \n")


    
    