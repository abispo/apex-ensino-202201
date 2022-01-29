from time import sleep
from random import randint


class Pagamento:

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def pagar(self):
        raise NotImplementedError("Não implementado")


class PagamentoPorCartao(Pagamento):

    def __init__(self, valor, parcelas):
        super().__init__(valor)
        self._parcelas = parcelas

    @property
    def parcelas(self):
        return self._parcelas

    @parcelas.setter
    def parcelas(self, parcelas):
        self._parcelas = parcelas

    def pagar(self):
        print("Conectando-se com o servidor...")
        sleep(randint(1, 5))
        input("Digite a senha... ")
        print("Validando...")
        sleep(randint(1, 5))
        print("Pagamento confirmado!")


class PagamentoPorBoleto(Pagamento):

    def __init__(self, valor, codigo_de_barras):
        super().__init__(valor)
        self._codigo_de_barras = codigo_de_barras

    @property
    def codigo_de_barras(self):
        return self._codigo_de_barras

    @codigo_de_barras.setter
    def codigo_de_barras(self, codigo_de_barras):
        self._codigo_de_barras = codigo_de_barras

    def pagar(self):
        print("Efetuando pagamento por boleto...")
        sleep(randint(1, 2))
        print("Pagamento confirmado!")

if __name__ == '__main__':

    # Exemplos de polimorfismo dentro do Python
    print(4 + 4)
    print("Curso" + " " + "Python")
    print("d"*10)

    print(len("Python"))
    print(len([1, 2, 5]))

    pagamento_por_cartao = PagamentoPorCartao(1200, 6)
    pagamento_por_cartao.pagar()

    pagamento_por_boleto = PagamentoPorBoleto(300, "34832808094u52b09asdfh0wqe4rh904fhbfe80sdafb")
    pagamento_por_boleto.pagar()