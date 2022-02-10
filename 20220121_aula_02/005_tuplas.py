# TUPLAS

# Tuplas são estruturas de dados em Python que são ordenadas, imutáveis e permites valores repetidos

if __name__ == '__main__':

    # Criando uma tupla
    items = ('Banana', 'Mamão',)
    print(items)

    # Lendo um item da tupla pelo seu índice
    print(items[0])

    # A linha abaixo causará a exceção 'TypeError', pois tuplas não permitem alteração de valores
    # items[1] = 'Laranja'

    # Existem algumas saídas que podemos usar quando queremos alterar algum valor da tupla
    lista_items = list(items)
    lista_items[1] = 'Laranja'
    items = tuple(lista_items)

    print(items)

    # Podemos também adicionar uma tupla a outra
    items_2 = ('Coco', 'Manga', 'Manga',)
    items += items_2

    print(items)

    # Assim como uma lista, uma tupla é uma sequência que pode ser iterada utilizando o laço for
    for item in items:
        print(item)

    # Podemos fazer também o 'unpacking', que nada mais é do que extrair os valores das tuplas e colocá-los
    # em variáveis

    (item_1, item_2, item_3, item_4, item_5) = items

    print(item_1, item_2, item_3, item_4, item_5)

    # Tuplas possuem apenas 2 métodos

    # count() -> Retorna a quantidade de vezes que um item aparece em uma tupla
    print(items.count('Manga'))

    # index() -> Procura na tupla por um valor específico e retorna a posição desse valor
    print(items)
    print(items.index('Manga'))