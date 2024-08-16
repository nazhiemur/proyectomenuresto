while True:
    try:
        colorelegido = int(input("\033[2;37m"+
            "Colores disponibles: \n  1 - Verde \n  2 - Amarillo \n  3 - Rojo \nElija un color:\n "+'\033[0;m'))
        if colorelegido == 1:
            print("\033[;32m"+"\nResultado: Puede Pasar\n"+'\033[0;m')
        elif colorelegido == 2:
            print("\033[;33m"+"\nResultado: Precaución\n"+'\033[0;m')
        elif colorelegido == 3:
            print("\033[;31m"+"\nResultado: No pasar\n"+'\033[0;m')
        elif colorelegido != int:
            print("\033[;31m"+"\nNo en rango\n"+'\033[0;m')
            break
        continue
    except ValueError:
        print("\n\n"+"\033[;31m"+"Debe ingresar un Color disponible. Elija con los numeros. Intente nuevamente\n"+'\033[0;m')
    continue