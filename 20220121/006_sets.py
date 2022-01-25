# Set (Conjunto) é uma estrutura de dados que é não ordenada, imutável e não indexável

if __name__ == '__main__':

    # Criando um set
    conjunto = {'Banana', 'Uva', 'Abacaxi'}

    # As linhas abaixo gerarão exceções de código, pois não conseguimos alterar o valor de um set pelo índice
    # tampouco ler os valores pelo índice (não indexável e imutável)
    #print(conjunto[1])
    #conjunto[1] = 1

    for item in conjunto:
        print(item)

    # add() -> Adicionar um novo item em um set
    conjunto.add('Melancia')
    print(conjunto)

    # update() -> Utilizamos update() quando queremos adicionar os valores de um conjunto ao outro
    conjunto_2 = {'Linguiça', 'Carne', 'Mortadela'}
    conjunto_2 = {'Abacaxi', 'Banana', 'Uva', 'Melancia'}


    conjunto.update(conjunto_2)
    print(conjunto)

    # remove() -> Remove um elemento do set
    conjunto.remove('Banana')
    print(conjunto)

    lista = [1, 1, 1, 1, 4, 4, 4, 5, 5, 3, 9]
    lista = list(set(lista))
    print(lista)

    # Pegando valores que se repetem nos 2 conjuntos
    numeros_1 = {1, 2, 3, 7, 6}
    numeros_2 = {4, 3, 9, 8, 1}

    resultado = numeros_1.intersection(numeros_2)

    print(resultado)