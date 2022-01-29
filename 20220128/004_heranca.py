
class Animal:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def info(self):
        return f"""
        Nome do Animal: {self.nome}
        Idade do Animal: {self.idade}
        """


class Cachorro(Animal):
    pass


class Gato(Animal):
    pass


class Pagamento:

    def __init__(self, valor=0):
        print("pagamento")
        self._valor = valor


class PagamentoPorBoleto(Pagamento):
    pass


class PagamentoPorCartao(Pagamento):

    def __init__(self, valor, parcelas):
        print("cartao")
        super().__init__(valor)
        self._parcelas = parcelas
        print("ok")


if __name__ == '__main__':

    cachorro = Cachorro('Rex', 5)
    gato = Gato('Mimi', 2)

    cachorro.nome = 'Trovão'

    print(cachorro.info())
    print(gato.info())

    pagamento_cartao = PagamentoPorCartao(1000, 10)
