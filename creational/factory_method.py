"""
    O Método de Fábrica é um padrão de design criacional que fornece uma 
    interface para criar objetos em uma superclasse, mas permite que as 
    subclasses alterem o tipo de objeto que será criado.
"""
from abc import ABC, abstractmethod

#===========================================Definição de classes abstratas
class Product(ABC):
    """ This class is used for implements a new product in the system """
    @abstractmethod
    def build_product(self) -> str:
        """ return the str building """
        pass

class Creator(ABC):
    """ This class is used for create of creators of products """
    @abstractmethod
    def create_product(self) -> Product:
        """ return the Product for building """
        pass

    def build(self) -> str:
        """ return the content build """
        _produto = self.create_product()
        return _produto.build_product()
#=========================================Definição dos Produtos concretos
class Product1(Product):

    def build_product(self) -> str:
        return "Product 1 Build"

class Product2(Product):

    def build_product(self) -> str:
        return "Product 2 Build"
#========================================Definição dos Creadores concretos
class CreatorProduct1(Creator):

    def create_product(self) -> Product1:
        return Product1()

class CreatorProduct2(Creator):

    def create_product(self) -> Product2:
        return Product2()
#======================================================Definição do Cliente
def fm_client(creator: Creator) -> None:
    print(creator.build())

def main_fm():
    while True:
        try:
            option = int(input("Criador option [1][2] | Exit[0]: "))
            if(option == 1):
                fm_client(CreatorProduct1())
            elif(option == 2):
                fm_client(CreatorProduct2())
            elif(option == 0):
                break
        except:
            print("Option false")
            continue
    




