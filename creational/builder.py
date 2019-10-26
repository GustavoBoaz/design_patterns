"""
    O Builder é um padrão de design criacional que permite construir objetos
    complexos passo a passo. O padrão permite produzir diferentes tipos e
    representações de um objeto usando o mesmo código de construção.

    Como Implementar:

    1.  Certifique-se de definir claramente as etapas comuns de construção
        para criar todas as representações de produtos disponíveis. Caso
        contrário, você não poderá prosseguir com a implementação do padrão.

    2.  Declare estas etapas na interface do construtor base.

    3.  Crie uma classe de construtor concreto para cada uma das representações
        do produto e implemente suas etapas de construção.

        Não se esqueça de implementar um método para buscar o resultado da
        construção. A razão pela qual esse método não pode ser declarado dentro
        da interface do construtor é que vários construtores podem construir
        produtos que não possuem uma interface comum. Portanto, você não sabe
        qual seria o tipo de retorno para esse método. No entanto, se você
        estiver lidando com produtos de uma única hierarquia, o método de busca
        poderá ser adicionado com segurança à interface base.

    4.  Pense em criar uma classe de diretor. Pode encapsular várias maneiras
        de construir um produto usando o mesmo objeto construtor.

    5.  O código do cliente cria os objetos construtor e diretor. Antes do início
        da construção, o cliente deve passar um objeto construtor para o diretor.
        Normalmente, o cliente faz isso apenas uma vez, através de parâmetros do
        construtor do diretor. O diretor usa o objeto construtor em todas as construções
        posteriores. Existe uma abordagem alternativa, na qual o construtor é
        passado diretamente para o método de construção do diretor.

    6.  O resultado da construção pode ser obtido diretamente do diretor apenas se
        todos os produtos seguirem a mesma interface. Caso contrário, o cliente deve
        buscar o resultado do construtor.
"""
from abc import ABC, abstractmethod
from typing import Any

#===========================================Definição de classes abstratas
class Builder(ABC):

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def build_step_A(self) -> None:
        pass

    @abstractmethod
    def build_step_B(self) -> None:
        pass

    @abstractmethod
    def build_step_C(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> None:
        pass
#=========================================Definição dos Produtos concretos
class Product1():

    def __init__(self):
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts Product1: {', '.join(self.parts)}", end="\n")

class Product2():

    def __init__(self):
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts Product2: {', '.join(self.parts)}", end="\n")
#===========================================Definição do Montador concreto
class Builder1(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product1 = Product1()

    def build_step_A(self) -> None:
        self._product1.add("PartA1")

    def build_step_B(self) -> None:
        self._product1.add("PartB1")

    def build_step_C(self) -> None:
        self._product1.add("PartC1")

    def get_result(self) -> None:
        self._product1.list_parts()

class Builder2(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product2 = Product2()

    def build_step_A(self) -> None:
        self._product2.add("PartA2")

    def build_step_B(self) -> None:
        self._product2.add("PartB2")

    def build_step_C(self) -> None:
        self._product2.add("PartC2")

    def get_result(self) -> None:
        self._product2.list_parts()
#=====================================================Definição do Diretor
class Director():

    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    def make(self) -> None:
        self._builder.reset()
        while True:
            try:
                option = input("Add Part [A][B][C] | Exit get Result[X]: ")
                if(option == "a"):
                    self._builder.build_step_A()
                    continue
                elif(option == "b"):
                    self._builder.build_step_B()
                    continue
                elif(option == "c"):
                    self._builder.build_step_C()
                    continue
                elif(option == "x"):
                    self._builder.get_result()
                    break
            except:
                print("Option false")
                continue
#=====================================================Definição do Cliente
def main_b():
    while True:
        try:
            option = int(input("Builder option [1][2] | Exit[0]: "))
            if(option == 1):
                Director(Builder1()).make()
            elif(option == 2):
                Director(Builder2()).make()
            elif(option == 0):
                break
        except:
            print("Option false")
            continue