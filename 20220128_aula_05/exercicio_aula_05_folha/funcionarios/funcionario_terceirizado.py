from .funcionario import Funcionario

class FuncionarioTerceirizado(Funcionario):

    def __init__(self, nome, qtd_horas_trabalhadas, valor_hora):

        super().__init__(nome)
        self._qtd_horas_trabalhadas = qtd_horas_trabalhadas
        self._valor_hora = valor_hora

    def calcular_salario(self):
        self._salario = self._qtd_horas_trabalhadas * self._valor_hora