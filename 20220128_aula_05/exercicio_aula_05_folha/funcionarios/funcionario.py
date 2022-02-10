from uuid import uuid4


class Funcionario:
    def __init__(self, nome):
        self._id = str(uuid4())
        self._nome = nome
        self._salario = 0

    def calcular_salario(self):
        pass

    def info(self):
        return f"""
        ID: {self._id}
        Nome: {self._nome}
        Salário: {self._salario}
        """

    def to_dict(self):
        return {
            'id': self._id,
            'nome': self._nome,
            'salario': f"{self._salario:.2f}"
        }