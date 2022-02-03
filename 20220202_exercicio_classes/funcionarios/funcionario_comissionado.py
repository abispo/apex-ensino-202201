from .funcionario import Funcionario

class FuncionarioComissionado(Funcionario):

    def __init__(self, nome, valor_total, porcentagem_comissao):
        super().__init__(nome)
        self._valor_total = valor_total
        self._porcentagem_comissao = porcentagem_comissao

    def calcular_salario(self):
        self._salario = self._valor_total * (self._porcentagem_comissao / 100)