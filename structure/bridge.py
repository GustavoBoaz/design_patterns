"""
    Bridge é um padrão de design estrutural que permite dividir uma classe grande
    ou um conjunto de classes estreitamente relacionadas em duas hierarquias
    separadas - abstração e implementação - que podem ser desenvolvidas
    independentemente uma da outra.

    COMO IMPLEMENTAR:

    1.  Identifique as dimensões ortogonais em suas aulas. Esses conceitos
        independentes podem ser: abstração / plataforma, domínio / infraestrutura,
        front-end / back-end ou interface / implementação.

    2.  Veja quais operações o cliente precisa e defina-as na classe de abstração
        básica.

    3.  Determine as operações disponíveis em todas as plataformas. Declare os que
        a abstração precisa na interface de implementação geral.

    4.  Para todas as plataformas do seu domínio, crie classes de implementação
        concretas, mas verifique se todas elas seguem a interface de implementação.

    5.  Dentro da classe de abstração, adicione um campo de referência para o tipo
        de implementação. A abstração delega a maior parte do trabalho ao objeto de
        implementação mencionado nesse campo.

    6.  Se você tiver várias variantes da lógica de alto nível, crie abstrações
        refinadas para cada variante estendendo a classe de abstração básica.

    7.  O código do cliente deve passar um objeto de implementação ao construtor da 
        abstração para associar um ao outro. Depois disso, o cliente pode esquecer a
        implementação e trabalhar apenas com o objeto de abstração.
"""

from abc import ABC, abstractmethod

#======================================Definição de classes abstratas (implementaçao)
class Implementation(ABC):
    @abstractmethod
    def method1(self) -> None:
        pass

    @abstractmethod
    def method2(self) -> None:
        pass

    @abstractmethod
    def method3(self) -> None:
        pass
#==========================================================Definição da implementaçao
class ConcreteImplementation(Implementation):

    def method1(self):
        print("Executado Metodo 1")

    def method2(self):
        print("Executado Metodo 2")

    def method3(self):
        print("Executado Metodo 3")
#===============================================================Definição da Abstração
class Abstraction():

    def __init__(self, implements: Implementation):
        self._implements = implements
    
    def feature1(self) -> None:
        self._implements.method1()

    def feature2(self) -> None:
        self._implements.method3()
        self._implements.method2() 
#=================================================================Definição do cliente
def main_b():
    while True:
        try:
            option = int(input("Caracteristica [1][2] | Exit[0]: "))
            if(option == 1):
                Abstraction(ConcreteImplementation()).feature1()
                continue
            elif(option == 2):
                Abstraction(ConcreteImplementation()).feature2()
                continue
            elif(option == 0):
                break
        except:
            print("Option false")
            continue