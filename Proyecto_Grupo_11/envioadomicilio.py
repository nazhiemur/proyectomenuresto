class FormaEntrega:
    """
    Clase para gestionar la selección del método de entrega del pedido.
    """

    def __init__(self):
        pass

    def seleccionar_entrega(self):
        """
        Función que presenta las opciones de entrega al usuario y devuelve la selección.

        Returns:
            str: 'domicilio' si el usuario elige envío a domicilio, 'retiro' si elige retiro en el local.
        """

        while True:
            print("Seleccione el método de entrega:")
            print("1. Envío a domicilio")
            print("2. Retiro en el local")
            opcion = input("Ingrese el número de la opción: ")

            if opcion == '1':
                return 'domicilio'
            elif opcion == '2':
                return 'retiro'
            else:
                print("Opción inválida. Por favor, ingrese 1 o 2.")