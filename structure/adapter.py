"""
    O adaptador é um padrão de design estrutural que permite a 
    colaboração de objetos com interfaces incompatíveis.

    COMO IMPLEMENTAR:

    1.  Verifique se você possui pelo menos duas classes com
        interfaces incompatíveis:

        Uma classe de serviço útil , que você não pode alterar
        (geralmente de terceiros, herdada ou com muitas dependências
        existentes).

        Uma ou várias classes de clientes que se beneficiariam do uso
        da classe de serviço.

    2.  Declare a interface do cliente e descreva como os clientes
        se comunicam com o serviço.

    3.  Crie a classe do adaptador e faça-a seguir a interface do 
        cliente. Deixe todos os métodos vazios por enquanto.

    4.  Adicione um campo à classe do adaptador para armazenar uma
        referência ao objeto de serviço. A prática comum é inicializar
        esse campo por meio do construtor, mas às vezes é mais conveniente
        passá-lo ao adaptador ao chamar seus métodos.

    5.  Um por um, implemente todos os métodos da interface do cliente na
        classe do adaptador. O adaptador deve delegar a maior parte do
        trabalho real ao objeto de serviço, manipulando apenas a conversão
        de interface ou formato de dados.

    6.  Os clientes devem usar o adaptador através da interface do cliente.
        Isso permitirá alterar ou estender os adaptadores sem afetar o
        código do cliente.
"""
from abc import ABC, abstractmethod

#===========================================Definição de classes abstratas
class ClienteIntegrate(ABC):
    @abstractmethod
    def integrate(self) -> None:
        """
            Metodo para integracao com o sistema cliente
        """
        self
#==============================================Definição do Serviço Padrão
class ServiceStandard(ClienteIntegrate):
    def integrate(self) -> None:
        print("Utilizando serviço Padrão!")
#=======================================Definição do Serviço para integrar
class ServiceIntegrate():
    def service_method(self) -> None:
        print("Utilizando serviço Integrado!")
#===================================Definição do Adaptador para integraçao
class Adapter(ClienteIntegrate):

    def __init__(self, adapter: ServiceIntegrate):
        self._adapter = adapter

    def integrate(self) -> None:
        return self._adapter.service_method()
#=====================================================Definição do Cliente
def a_client(client: ClienteIntegrate):
    client.integrate()

def main_a():
    while True:
        try:
            option = int(input("Serviço padrão [1] | Serviço Integrado [2] | Exit[0]: "))
            if(option == 1):
                a_client(ServiceStandard())
            elif(option == 2):
                a_client(Adapter(ServiceIntegrate()))
            elif(option == 0):
                break
        except:
            print("Option false")
            continue