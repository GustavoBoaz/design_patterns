from abc import ABC, abstractmethod

#===========================================Definição de classes abstratas
class ProductA(ABC):
    """ This class is used for implements a new product in the system """
    @abstractmethod
    def build_productA(self) -> str:
        """ return the str building """
        pass

class ProductB(ABC):
    """ This class is used for implements a new product in the system """
    @abstractmethod
    def build_productB(self) -> str:
        """ return the str building """
        pass

class AbstractFactory(ABC):
    """ This class is used for call method of creation of in the product in the system """
    @abstractmethod
    def create_productA(self) -> ProductA:
        """ return the ProductA building """
        pass

    @abstractmethod
    def create_productB(self) -> ProductB:
        """ return the ProductB building """
        pass
#=========================================Definição dos Produtos concretos
class ProductA1(ProductA):

    def build_productA(self) -> str:
        return "Concrete ProductA1 Build!"

class ProductB1(ProductB):

    def build_productB(self) -> str:
        return "Concrete ProductB1 Build!"

class ProductA2(ProductA):

    def build_productA(self) -> str:
        return "Concrete ProductA2 Build!"

class ProductB2(ProductB):

    def build_productB(self) -> str:
        return "Concrete ProductB2 Build!"
#=========================================Definição dos Fabricas concretas
class Factory1(AbstractFactory):

    def create_productA(self) -> ProductA:
        return ProductA1()

    def create_productB(self) -> ProductB:
        return ProductB1()

class Factory2(AbstractFactory):

    def create_productA(self) -> ProductA:
        return ProductA2()

    def create_productB(self) -> ProductB:
        return ProductB2()
#======================================================Definição do Cliente
def af_client(abstract_factory: AbstractFactory) -> None:
    while True:
        try:
            option = input("Criador produto [A][B] | Exit[C]: ")
            if(option == "a"):
                print(abstract_factory.create_productA().build_productA())
            elif(option == "b"):
                print(abstract_factory.create_productB().build_productB())
            elif(option == "c"):
                break
        except:
            print("Option false")
            continue

def main_af():
    while True:
        try:
            option = int(input("Fabrica option [1][2] | Exit[0]: "))
            if(option == 1):
                af_client(Factory1())
            elif(option == 2):
                af_client(Factory2())
            elif(option == 0):
                break
        except:
            print("Option false")
            continue