"""
    O Método de Fábrica é um padrão de design criacional que fornece uma 
    interface para criar objetos em uma superclasse, mas permite que as 
    subclasses alterem o tipo de objeto que será criado.

    Como Implementar:

    1.  Faça com que todos os produtos sigam a mesma interface. Essa interface
        deve declarar métodos que fazem sentido em todos os produtos.

    2.  Adicione um método de fábrica vazio dentro da classe criador. O tipo de
        retorno do método deve corresponder à interface comum do produto.

    3.  No código do criador, encontre todas as referências aos construtores de
        produtos. Um por um, substitua-os por chamadas para o método de fábrica,
        enquanto extrai o código de criação do produto para o método de fábrica.
        
        Pode ser necessário adicionar um parâmetro temporário ao método de fábrica
        para controlar o tipo de produto retornado.

        Neste ponto, o código do método de fábrica pode parecer bastante feio. Pode
        ter um grande switchoperador que escolhe qual classe de produto instanciar.
        Mas não se preocupe, resolveremos isso em breve.

    4.  Agora, crie um conjunto de subclasses de criador para cada tipo de produto
        listado no método de fábrica. Substitua o método de fábrica nas subclasses
        e extraia os bits apropriados do código de construção do método base.

    5.  Se houver muitos tipos de produtos e não fizer sentido criar subclasses para
        todos eles, você poderá reutilizar o parâmetro de controle da classe base nas
        subclasses.

        Por exemplo, imagine que você tenha a seguinte hierarquia de classes: a Mailclasse
        base com algumas subclasses: AirMaile GroundMail; as Transportaulas são Plane,
        Trucke Train. Enquanto a AirMailclasse usa apenas Planeobjetos, GroundMailpode
        funcionar com ambos Trucke Trainobjetos. Você pode criar uma nova subclasse
        (digamos TrainMail) para lidar com os dois casos, mas há outra opção. O código
        do cliente pode passar um argumento para o método de fábrica da GroundMailclasse
        para controlar qual produto ele deseja receber.

    6.  Se, após todas as extrações, o método base de fábrica ficar vazio, você poderá
        torná-lo abstrato. Se sobrar algo, você pode torná-lo um comportamento padrão do
        método.
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
    




