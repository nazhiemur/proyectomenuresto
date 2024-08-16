#Pedido de datos al usuario
numeros_ingresados = int(input("Cuantos numeros desea ingresar?"))
lista = []
for numeros_ingresados in range (0,numeros_ingresados):
    lista.append(int(input('Ingrese Valor: ')))

#Ordenamiento Burbuja
for numPasada in range(len(lista)-1,0,-1):
        for i in range(numPasada):
            print(i,end="\r")
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

#imprimir resultado
print(lista)