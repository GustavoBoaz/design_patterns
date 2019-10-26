"""
    Prototype é um padrão de design criacional que permite copiar objetos
    existentes sem tornar seu código dependente de suas classes.
"""
from abc import ABC, abstractmethod

#===========================================Definição de classes abstratas
class Prototype(ABC):
    
    @abstractmethod
    def clone(self) -> None:
        pass
#========================================Definição do Prototipo do Produto
class ProductPrototype1(Prototype):

    def __init__(self, value = None):
        self._iten = value

    @property
    def iten(self) -> None:
        print("Getting: {}".format(self._iten))
        return self._iten

    @iten.setter
    def iten(self, value) -> None:
        print("Setting: {}".format(value))
        self._iten = value

    @iten.deleter
    def iten(self):
        print("Deleting: {}".format(self._iten))
        del self._iten

    def clone(self):
        return ProductPrototype1(self._iten)
#=====================================================Definição do Cliente
def main_p():
    while True:
        try:
            option = int(input("Clonar option [1] | Exit[0]: "))
            if(option == 1):
                clone0 = ProductPrototype1() #Instancia Produto Prototipo
                clone1 = clone0.clone() # Clonando produto para um novo objeto

                print("Valor do Iten Padrão: {}".format(clone0._iten))
                print("Valor do Iten Clonado: {}\n".format(clone1._iten))

                value = int(input("Inserir valor novo no clone: "))
                clone1.iten = value

                print("Valor do Iten Padrão: {}".format(clone0._iten))
                print("Valor do Iten Clonado: {}".format(clone1._iten))

                del clone0.iten
                del clone1.iten
            elif(option == 0):
                break
        except:
            print("Option false")
            continue

