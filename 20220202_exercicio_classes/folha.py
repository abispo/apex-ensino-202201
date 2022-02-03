import csv
from datetime import datetime


class FolhaDePagamento:

    def __init__(self, lista_funcionarios=[]):
        self._lista_de_funcionarios = lista_funcionarios[:]

    def adicionar(self, funcionario):
        self._lista_de_funcionarios.append(funcionario)

    def processar(self):
        for funcionario in self._lista_de_funcionarios:
            funcionario.calcular_salario()
            print(funcionario.info())

    def salvar(self):

        nome_arquivo = f"folha_funcionarios_{datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')}.csv"

        cabecalho = ["id", "nome", "salario"]

        with open(nome_arquivo, mode='w', newline='', encoding="utf-8") as _file:
            writer = csv.DictWriter(_file, delimiter=';', fieldnames=cabecalho)
            writer.writeheader()

            for funcionario in self._lista_de_funcionarios:
                writer.writerow(funcionario.to_dict())
