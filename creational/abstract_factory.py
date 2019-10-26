"""
    Abstract Factory é um padrão de design criacional que permite produzir
    famílias de objetos relacionados sem especificar suas classes concretas.

    Como Implementar:
    
    1.  Mapeie uma matriz de tipos de produtos distintos versus variantes
        desses produtos.

    2.  Declare interfaces abstratas do produto para todos os tipos de produtos.
        Em seguida, faça com que todas as classes de produtos concretas
        implementem essas interfaces.

    3.  Declare a interface abstrata de fábrica com um conjunto de métodos de
        criação para todos os produtos abstratos.

    4.  Implemente um conjunto de classes de fábrica de concreto, uma para cada
        variante de produto.

    5.  Crie o código de inicialização de fábrica em algum lugar do aplicativo.
        Ele deve instanciar uma das classes de fábrica de concreto, dependendo da
        configuração do aplicativo ou do ambiente atual. Passe esse objeto de
        fábrica para todas as classes que constroem produtos.

    6.  Examine o código e encontre todas as chamadas diretas para os construtores
        de produtos. Substitua-os por chamadas para o método de criação apropriado
        no objeto de fábrica.
"""
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