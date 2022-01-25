# Dicionários
# Um dicionário é um tipo de estrutura de dados em Python que serve pra armazenar dados no formato chave: valor

if __name__ == '__main__':

    joao = {
        'nome': 'João da Silva',
        'idade': 40,
        'genero': 'M',
        'funcoes': ['mecanico', 'manobrista'],
        'dicio': {'chave': 'valor'}
    }

    print(joao)

    # Precisamos informar o índice do dicionário para acessar o seu valor
    print(joao['funcoes'])

    # Podemos acessar o valor usando o método get
    print(joao.get('funcoesd'))

    # Se a chave não existir, podemos definir um valor padrão que será retornado
    print(joao.get('essa-chave-nao-existe', 'Inexistente'))

    # Podemos usar os métodos keys() e values() para retornar as chaves e os valores, respectivamente.

    print(joao.keys())
    print(joao.values())

    # Usando os operadores de pertencimento pra verificar a existência de chaves e valores
    print('profissao' in joao.keys())
    print(20 not in joao.values())

    # ATUALIZANDO DADOS DE UM DICIONÁRIO
    joao['idade'] = 30
    print(joao)

    endereco = {
        'endereco': {
            'logradouro': 'rua',
            'endereco': 'Rua XV de Novembro, 100',
            'cidade': 'blumenau'
        }
    }

    # Podemos usar o método update() pra atualizar o dicionário utilizando outro dicionário
    joao.update(endereco)
    print(joao)

    # REMOVENDO ITENS DE UM DICIONÁRIO

    # O método pop(<chave>) remove a dupla chave-valor especificada pela chave
    joao.pop('dicio')
    print(joao)

    # O método popitem() remove sempre a última chave do dicionário.
    joao.popitem()
    print(joao)

    # Podemos usar a palavra-chave del
    # Pode ser usado também em listas

    # Excluindo a chave funcoes
    del joao['funcoes']

    print(joao)

    # del pode também excluir o objeto inteiro
    # del joao

    print(joao)

    # Iterando sobre os itens de um dicionário
    # Da maneira padrão são retornadas apenas as chaves
    # Também podemos usar o método keys() pra retornar as chaves

    #for item in joao:
    for key in joao.keys():
        print(key)

    # Podemos percorrer apenas os valores do nosso dicionário
    for value in joao.values():
        print(value)

    # Podemos retornar tanto chave quanto valor no mesmo for
    for key, value in joao.items():         # unpack de tuplas
        print(f"Chave: {key} | Valor: {value}")

    jose = joao.copy()
    jose['idade'] = 20

    print(joao)
    print(jose)