
'''
8) Hacer un programa que cuente del 1 al 100 inclusive e imprima los números que son
divisibles por 2 y por 5.
'''
# for i in range(101):
#     if i % 2 == 0 and i % 5 == 0:
#         print(i)


'''
9) Hacer un programa que imprima una tabla de multiplicar del 2 al 9 . Cada uno debe
mostrar sus valores multiplicados del 1 al 9 inclusive
'''
# # #for
# for i in range(2, 10):
#     for j in range(10):
#         print( "tabla del ", i , "x", j, "=", i * j)
#     print("--------------------------------------------")

# # #while



'''
10) Hacer un programa que muestre el siguiente dibujo.
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
 * * * * * * * * * *
'''
# for i in range(5):
#     for j in range(10):
#         print("* ", end="")
#     print()


 
''' 
11) Hacer un programa donde se muestre el siguiente dibujo

 * * * * * * * * * *
 * *
 * *
 * *
 * * * * * * * * * *
'''
# for i in range(5):
#     if i == 0 or i == 4:
#         for j in range(10):
#             print("* ", end="")
#         print()
#     else:
#         for j in range(2):
#             print("* ", end="")
#         print()

 

'''
12)Hacer un programa que muestre el siguiente dibujo
 *
 * *
 * * *
 * * * *
 * * * * *
'''

# for i in range(5):
#     print("* " * (i + 1), end="")
#     print()


''' 
13) Idem anterior con este dibujo
 * * * * *
 * * * *
 * * *
 * *
 *
 '''

# for i in range(5):
#     print("* " * (5 - i), end="")
#     print()