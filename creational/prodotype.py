"""
    Prototype é um padrão de design criacional que permite copiar objetos
    existentes sem tornar seu código dependente de suas classes.

    Como Implementar:

    1.  Crie a interface do protótipo e declare o clonemétodo nela. Ou
        apenas adicione o método a todas as classes de uma hierarquia de
        classes existente, se você tiver uma.

    2.  Uma classe de protótipo deve definir o construtor alternativo que
        aceita um objeto dessa classe como argumento. O construtor deve copiar
        os valores de todos os campos definidos na classe do objeto passado
        para a instância recém-criada. Se você estiver alterando uma subclasse,
        deverá chamar o construtor pai para permitir que a superclasse manipule
        a clonagem de seus campos privados.

        Se sua linguagem de programação não suportar sobrecarga de método, você
        poderá definir um método especial para copiar os dados do objeto. O
        construtor é um local mais conveniente para fazer isso porque ele entrega
        o objeto resultante logo após a chamada do newoperador.

    3.  O método de clonagem geralmente consiste em apenas uma linha: executar
        um newoperador com a versão prototípica do construtor. Observe que toda
        classe deve substituir explicitamente o método de clonagem e usar seu
        próprio nome de classe junto com o newoperador. Caso contrário, o método
        de clonagem pode produzir um objeto de uma classe pai.

    4.  Opcionalmente, crie um registro de protótipo centralizado para armazenar
        um catálogo de protótipos usados ​​com freqüência.

        Você pode implementar o registro como uma nova classe de fábrica ou
        colocá-lo na classe de protótipo de base com um método estático para buscar
        o protótipo. Este método deve procurar um protótipo com base nos critérios
        de pesquisa que o código do cliente passa para o método. Os critérios podem
        ser uma tag de cadeia simples ou um conjunto complexo de parâmetros de
        pesquisa. Depois que o protótipo apropriado for encontrado, o registro deve
        cloná-lo e devolver a cópia ao cliente.

        Por fim, substitua as chamadas diretas aos construtores das subclasses pelas
        chamadas ao método de fábrica do registro do protótipo.
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

