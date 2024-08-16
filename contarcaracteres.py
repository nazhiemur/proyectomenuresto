#  Ejercicio 2: Contar caracteres
# cantidad_caracteres = len("astronomico")
# print(cantidad_caracteres)

texto = input("Introducir el texto: ")

cantidad_caracteres = 0

for i in texto:
    # print(i)
    if i != " ":
        cantidad_caracteres = cantidad_caracteres + 1

print("la cantidad de caracteres del texto es: ", cantidad_caracteres)