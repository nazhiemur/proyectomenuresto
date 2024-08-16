while True:
    try:
        numero_1 = int(input("Ingrese su edad en numeros: "))
    except ValueError:
        print("Debe ingresar un numero entero. Intente nuevamente")
        continue
    if numero_1 > 17:
        print("Es mayor")
        break
    else: 
        print("Es menor")
        break 