import random
#importamos random para generar numero de pedido
class SeleccionEntrega:
       
    def __init__(self):
                
        self.numero_pedido = random.randint(0,9999)

    def seleccionar_entrega(self):
            
        while True:
            print("Selecciona como queres recibir tu pedido:")
            print("1. Te mandamos a domicilio")
            print("2. Retiras del local")
            opcion = input("\nElegí tu opción preferida: ")

            if opcion == '1':
                # Solicitar la dirección de envío
                direccion = input("Dirección donde enviamos: ")
                print(f"\n¡Tu pédido {self.numero_pedido} esta confirmado! Te lo mandamos a : {direccion}\n")
                return 'domicilio'
            elif opcion == '2':
                print(f"\n¡Tu pedido {self.numero_pedido} te espera en el local, podes pasar a retirarlo desde las XX\n") 
                return 'retiro'
            else:
                print("\nOpción inválida. Por favor, ingrese 1 o 2.\n")

    def envio_domicilio(self):
        pass
#Se genera un nro aleatorio para el pedido
SeleccionEntrega().seleccionar_entrega()
