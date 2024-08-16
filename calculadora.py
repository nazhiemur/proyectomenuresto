# con 2 numeros calcular todas las operaciones matematicas simples
while True:
    try:
        numero_1 = int(input("Ingrese el primer numero para calcular: "))
        numero_2 = int(input("Ingrese el segundo numero para calcular: "))
        print("El primer numero ingresado es: ", numero_1, "\nEl segundo numero es:",
              numero_2, "\n Ahora hare los calculos solicitados por la consigna")
    except ValueError:
        print("Debe ingresar un numero entero. Intente nuevamente")
        continue
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multi = numero_1 * numero_2
    divi = numero_1 / numero_2
    print("La suma de los numeros es: ", suma, "\nLa resta de los numeros es: ", resta,
          "\nLa multiplicación de los numeros es: ", multi, "\nLa división de los numero es: ", divi)