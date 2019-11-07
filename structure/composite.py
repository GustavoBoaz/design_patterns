"""
    Composite é um padrão de design estrutural que permite compor objetos
    em estruturas de árvores e trabalhar com essas estruturas como se
    fossem objetos individuais.

    COMO IMPLEMENTAR:

    1.  Verifique se o modelo principal do seu aplicativo pode ser representado
        como uma estrutura em árvore. Tente dividi-lo em elementos e recipientes
        simples. Lembre-se de que os contêineres devem poder conter elementos
        simples e outros contêineres.

    2.  Declare a interface do componente com uma lista de métodos que fazem
        sentido para componentes simples e complexos.

    3.  Crie uma classe folha para representar elementos simples. Um programa pode
        ter várias classes de folhas diferentes.

    4.  Crie uma classe de contêiner para representar elementos complexos. Nesta
        classe, forneça um campo de matriz para armazenar referências a subelementos.
        A matriz deve poder armazenar folhas e contêineres, portanto, certifique-se
        de que seja declarada com o tipo de interface do componente.

        Ao implementar os métodos da interface do componente, lembre-se de que um
        contêiner deve delegar a maior parte do trabalho em subelementos.

    5.  Por fim, defina os métodos para adicionar e remover elementos filho no contêiner.

        Lembre-se de que essas operações podem ser declaradas na interface do
        componente. Isso violaria o Princípio de Segregação de Interface, porque os
        métodos estarão vazios na classe folha. No entanto, o cliente poderá tratar
        todos os elementos igualmente, mesmo ao compor a árvore.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
#===========================================================Definição de classe abstrata
class Component(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass
#========================Definição de classe concreta Leaf(Simples) e Composite(Complexa) 
class Leaf(Component):
    
    def operation(self) -> str:
        return "Folha"

class Composite(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def is_composite(self) -> bool:
        return True
    
    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"
#====================================================================Definição do cliente
def c_client(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")

def main_c():
    tree = Composite()
    while True:
        try:
            option = int(input("Criar Novo Ramo[1] | Mostrar Arvore e Fechar[0]: "))
            if(option == 1):
                branch = Composite()
                while True:
                    option2 = int(input("ADD Folha [4] | Voltar[0]: "))
                    if(option2 == 4):
                        branch.add(Leaf())
                        continue
                    elif(option2 == 0):
                        tree.add(branch)
                        break
            elif(option == 0):
                c_client(tree)       
                break
        except:
            print("Option false")
            continue
        
