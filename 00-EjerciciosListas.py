# Ejercicios de listas (Utilizar todo lo aprendido hasta la ultima clase Variables/Operadores/Condicionales/Bucles/Listas/Metodos)
# Ejercicio 1
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
# y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

lista_aleatoria = [1,2,3,4,5,6,7,8,9,10]
for i in lista_aleatoria:
    print("El elemento es:",i, "\n", "Su Cuadrado es:", i**2, "\n","Su Cubo:", i**3)


# Ejercicio 2
# Crea una lista e inicializala con 5 cadenas de caracteres ingresadas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

# lista = []

# for i in range(5):
#     lista.append(input("Ingrese una palabra: "))

# print(lista)
# nueva_lista = lista.copy()
# print(nueva_lista)
# nueva_lista.reverse()
# print(nueva_lista)


# Ejercicio 3
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

# notas = []

# for i in range(5):
#     notas.append(float(input("Ingrese una nota: ")))

# print(notas)
# nota_media = sum(notas)/len(notas)
# print("La nota media es:", nota_media)
# print("La nota mas alta es:", max(notas))
# print("La nota mas baja es:", min(notas))


# Ejercicio 4
# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. 
# Entonces se debe imprimir el vector (sólo los elementos introducidos).
# lista = []
# while True:
#     numero = int(input("Ingrese un numero: "))
#     if numero < 0:
#         break
#     lista.append(numero)
# print(lista)
