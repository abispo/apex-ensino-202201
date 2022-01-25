# Listas
# Listas são um tipo de estrutura de dados do Python que servem para armazenar múltiplos valores. Esses valores podem
# ser de qualquer tipo, inclusive outras listas.

if __name__ == '__main__':

    exemplo_lista = [2.4, 5, 'Curso de Python', [1, 2, 3]]
    # exemplo_lista = list()

    # A função type mostra o tipo de objeto
    print(type(exemplo_lista))

    print(exemplo_lista)

    # Uma lista é um objeto indexado (ou indexável), ou seja, conseguimos acessar o qualquer valor dentro da lista
    # informando o índice desse valor.
    # Uma lista sempre começa com o índice 0. No exemplo abaixo, para acessarmos o terceiro item da lista, temos
    # que informar o índice 2
    print(exemplo_lista[0])

    # Podemos acessar um valor dentro de uma lista passando um índice negativo
    # O índice negativo sempre começa com -1

    #               0        1         2        3       4
    # lista1 = ['Banana', 'Arroz', 'Azeite', 'Coco', 'Carne']
    #             -5         -4       -3       -2       -1

    # Acessando o último item da lista utilizando índice negativo
    print(exemplo_lista[-1][-1])
    print(exemplo_lista[-2].upper())

    # Uma lista é também um objeto mutável, ou seja, podemos alterar os seus valores.

    # Alterando o último item da nossa lista utilizando o índice
    exemplo_lista[3] = 'Apex Ensino'
    print(exemplo_lista)

    # ADICIONANDO NOVOS VALORES EM UMA LISTA
    ########################################
    # append(<item>) -> Adiciona novos itens no final da lista
    lista_de_compras = ['Banana', 'Manga', 'Batata', 'Uva']
    print(lista_de_compras)
    lista_de_compras.append('Linguiça')
    print(lista_de_compras)

    # insert(<indice>, <item>) -> Adiciona um novo item na lista em uma posição específica
    lista_de_compras.insert(1, 'Pão')
    print(lista_de_compras)

    # extend(<list>) -> Extende os valores de uma lista usando outra lista
    laticinios = ['Queijo', 'Manteiga', 'Nata']
    lista_de_compras.extend(laticinios)
    print(lista_de_compras)

    # REMOVENDO ITENS DE UMA LISTA
    ################################

    # remove(<item>) -> Remove o item especificado da lista
    lista_de_compras.remove('Pão')
    print(lista_de_compras)

    # pop(<indice>) -> Remove um item da lista pelo seu índice
    lista_de_compras.pop(2)
    print(lista_de_compras)

    # Se não especifircarmos o índice, o método pop() remove o último item da lista
    lista_de_compras.pop()
    print(lista_de_compras)

    # Copiando listas
    print()

    lista_notas_aluno_a = [8, 6, 9]
    lista_notas_aluno_b = lista_notas_aluno_a

    print(lista_notas_aluno_a)
    print(lista_notas_aluno_b)

    lista_notas_aluno_b[2] = 10
    print(lista_notas_aluno_a)
    print(lista_notas_aluno_b)

    # Posição de memória 0x27435584
    # Valor armazenado [8, 6, 10]

    # Primeiro método de cópia de listas: método copy()
    lista_notas_aluno_c = lista_notas_aluno_a.copy()
    lista_notas_aluno_c[1] = 5
    print(f"Notas aluno A: {lista_notas_aluno_a}.")
    print(f"Notas aluno B: {lista_notas_aluno_b}.")
    print(f"Notas aluno C: {lista_notas_aluno_c}.")

    # Segundo método de cópia de listas: A chamada list()
    lista_notas_aluno_d = list(lista_notas_aluno_c)
    lista_notas_aluno_d[1] = 10
    print(f"Notas aluno A: {lista_notas_aluno_a}.")
    print(f"Notas aluno B: {lista_notas_aluno_b}.")
    print(f"Notas aluno C: {lista_notas_aluno_c}.")
    print(f"Notas aluno D: {lista_notas_aluno_d}.")

    # Terceiro método de cópia de listas: Utilizar slice
    lista_notas_aluno_e = lista_notas_aluno_d[:]
    lista_notas_aluno_e[0] = 10
    print(f"Notas aluno A: {lista_notas_aluno_a}.")
    print(f"Notas aluno B: {lista_notas_aluno_b}.")
    print(f"Notas aluno C: {lista_notas_aluno_c}.")
    print(f"Notas aluno D: {lista_notas_aluno_d}.")
    print(f"Notas aluno E: {lista_notas_aluno_e}.")

    print()
    # Slice de listas
    print(lista_de_compras)

    # Pegando todos os itens da lista, com exceção dos 2 primeiros
    print(lista_de_compras[2:])

    # Pegando todos os itens da lista entre o indice 2 e 4
    print(lista_de_compras[2:5])

    # Ordenar uma lista
    lista_notas_aluno_c.sort()

    # Por padrão, se uma lista possuir apenas valores numéricos, ela é ordenada do menor pro maior
    print(lista_notas_aluno_c)

    lista_notas_aluno_c.sort(reverse=True)
    print(lista_notas_aluno_c)

    # List comprehension
    lista_numeros = []
    for i in range(11):
        lista_numeros.append(i)

    print(lista_numeros)

    lista_numeros.clear()

    lista_numeros = [x for x in range(11)]
    print(lista_numeros)
