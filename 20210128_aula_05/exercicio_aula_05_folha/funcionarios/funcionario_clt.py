from .funcionario import Funcionario

class FuncionarioCLT(Funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome)
        self._salario = salario