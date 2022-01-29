
# Caixa Eletrônico

class CaixaEletronico:

    def __init__(self):
        self._saldo = 0
        self._arquivo_historico = 'historico_saldo.txt'

    def sacar(self, quantia):
        self._saldo = self._saldo - quantia
        self._salvar_historico_saldo()

    def depositar(self, quantia):
        self._saldo = self._saldo + quantia
        self._salvar_historico_saldo()

    def _salvar_historico_saldo(self):
        with open(self._arquivo_historico, mode='a') as _file:
            _file.write(str(f"{self._saldo}\n"))

    def visualizar_saldo(self):
        return f"Seu saldo é de: {self._saldo}"

    def entrar_na_conta(self, numero, senha):
        pass


class Pessoa():
    def __init__(self, nome="", idade=0):
        self._nome = nome
        self._idade = idade

    # Getters
    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    # Setters
    def set_nome(self, nome):
        self._nome = nome

    def set_idade(self, idade):
        self._idade = idade

    # Os getters e setters dentro do Python podem ser feitos usando @property

    # property é um decorator (decorador)
    # decorators sempre começam com @
    @property
    def idade(self):
        print("Chamando getter")
        return self._idade

    @idade.setter
    def idade(self, idade):
        print("Chamando setter")
        self._idade = idade


if __name__ == '__main__':
    pessoa = Pessoa()
    pessoa.idade = 10
    print(pessoa.idade)

    caixa = CaixaEletronico()
    caixa.depositar(1000)
    caixa.sacar(800)
    caixa.depositar(250)

    print(caixa.visualizar_saldo())