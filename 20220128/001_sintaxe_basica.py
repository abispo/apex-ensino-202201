
# declaração da classe
class Pessoa:

    # Método da classe Pessoa
    # O método construtor de classes em Python é o método __init__. É a partir dele que podemos definir
    # valores e ações a serem executadas no momento que o objeto é criado.
    def __init__(self, nome):
        print(self)
        # self representa o próprio objeto que está sendo criado.
        self._nome = nome
        self.cpf = "84930398843"

    # Método correr()
    def correr(self, km=10):
        print(f"{self._nome} está correndo {km} kms.")


if __name__ == '__main__':

    # laura é uma instância da classe Pessoa
    laura = Pessoa('Laura')
    joao = Pessoa('João')

    print(laura._nome)
    laura.correr(km=15)
    joao.correr()
    # print(dir(laura))