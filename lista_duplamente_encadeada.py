
class Elemento:

    def __init(self, valor):
        self.__valor = valor
        self.__anterior = None
        self.__proximo = None

    @property
    def valor(self):
        return self.__valor

    @property
    def anterior(self):
        return self.__anterior

    @property
    def proximo(self):
        return self.__proximo

class ListaDuplamenteEncadeada:

    def __init__(self, tamanho):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = tamanho

    def acessar_atual(self):
        pass

