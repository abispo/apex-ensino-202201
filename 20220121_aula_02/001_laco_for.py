
# Laço for (ou for loop)
# Um laço for é usado pra iterar sobre uma sequência (acessar sequencialmente os itens de uma
# sequência/container

if __name__ == '__main__':

    # Essa é uma lista
    lista_de_compras = ['Banana', 'Abacaxi', 'Manga', 'Uva']

    # Vamos usar o laço for pra percorrer essa lista, imprimindo no terminal item por item.
    for item in lista_de_compras:
        print(item)

    # Sempre que o for terminar com sucesso, o código dentro de else será executado
    else:
        print("Lista de compras lida.")

    # break | continue

    # Se o item manga for encontrado, o laço for é finalizado
    for item in lista_de_compras:
        if item == 'Manga':
            print("Retire a manga da lista")
            break

    # Se o item abacaxi for encontrado, não o imprima no terminal

    for item in lista_de_compras:
        if item == 'Abacaxi':
            continue
        print(item)


    # Iterando sobre uma sequência de número
    for numero in range(10):
        print(numero)

    # Exercício 01
