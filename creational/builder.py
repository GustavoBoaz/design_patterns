"""
    O Builder é um padrão de design criacional que permite construir objetos
    complexos passo a passo. O padrão permite produzir diferentes tipos e
    representações de um objeto usando o mesmo código de construção.
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