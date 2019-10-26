"""
    Singleton é um padrão de design criacional que permite garantir que uma
    classe tenha apenas uma instância, enquanto fornece um ponto de acesso
    global a essa instância.
"""
#===========================================Definição de classes Singleton
class Singleton(object):
    _instance = None

    def __new__(self):
        if (not self._instance):
            self._instance = super(Singleton, self).__new__(self)
            self._var = 10
        return self._instance

#==================Definição de metodo Singleton como Decorator de Classes
def singleton(myClass):
    instances = {}
    def get_instance(*args, **kwargs):
        if(myClass not in instances):
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return get_instance

@singleton #decorador ativado
class ProductSingleton(object):
    
    def __init__(self, value = None):
        self._value = value
    
    @property
    def iten(self) -> None:
        print("Getting value: {}".format(self._value))
        return self._value

    @iten.setter
    def iten(self, value) -> None:
        print("Setting value: {}".format(value))
        self._value = value

    @iten.deleter
    def iten(self):
        print("Deleting value: {}".format(self._value))
        del self._value
#=====================================================Definição do Cliente
def main_s():
    while True:
        try:
            option = int(input("Criar Singleton: Apartir de Classe [1] | Apartir de Decorador [2]  | Exit[0]: "))
            if(option == 1):
                instancia0 = Singleton()
                print("Instancia0 com Valor: {}".format(str(instancia0._var)))
                instancia0._var = int(input("Alterar Valor do iten: "))
                print("Valor alterado para: {}".format(str(instancia0._var)))
                instancia1 = Singleton()
                print("\nCriado nova instancia de Singleton")
                print("Instancia1 com Valor: {}".format(str(instancia1._var)))     
                continue
            elif(option == 2):
                instancia0 = ProductSingleton()
                instancia0.iten
                instancia0.iten = int(input("Alterar Valor do iten: "))
                print("\nCriado nova instancia de Singleton")
                instancia1 = ProductSingleton()
                instancia1.iten
                continue
            elif(option == 0):
                break
        except:
            print("Option false")
            continue