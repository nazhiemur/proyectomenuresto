
# Ejercicio 2: contar pares e impares de 10 numeros
pares = 0
impares = 0
for i in range(10):
    # ingreso de datos (Entrada)
    try:
        numero_ingresado = int(input("Introducir un numero: "))
    # estudio de si es par o impar (condicional)
        if numero_ingresado % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    except ValueError:
        print("Numero dije")
        continue
print("La cantida de numeros pares es: ", pares)
print("La cantida de numeros impares es: ", impares)
