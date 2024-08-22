import SeleccionEntrega
from lista_comidas import menusero

class main:
    def __init__(self):
        self.envio = SeleccionEntrega.SeleccionEntrega.seleccionar_entrega

    def tipoenvio(self):
        while True:
            if self.envio == "domicilio":
                print(menusero.listamenu)
            else :
                pass
                

main.tipoenvio