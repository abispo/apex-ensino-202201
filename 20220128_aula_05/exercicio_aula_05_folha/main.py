
from folha import FolhaDePagamento
from funcionarios import (
    FuncionarioCLT, FuncionarioTerceirizado, FuncionarioComissionado
)


if __name__ == '__main__':

    joao = FuncionarioCLT('João', 1800)
    maria = FuncionarioTerceirizado("Maria", 100, 75)
    lorena = FuncionarioComissionado("Lorena", 109453, 20)
    luiza = FuncionarioCLT("Luiza", 2800)
    carla = FuncionarioTerceirizado("Carla", 120, 85)

    lista_funcionarios = [joao, luiza, carla]

    folha_de_pagamento = FolhaDePagamento(lista_funcionarios)

    folha_de_pagamento.adicionar(maria)
    folha_de_pagamento.adicionar(lorena)

    folha_de_pagamento.processar()
    folha_de_pagamento.salvar()
