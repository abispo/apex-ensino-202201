
def exercicio_04(lista_de_numeros):
    lista_saida = []

    # for comum
    for numero in lista_de_numeros:
        # Vamos utilizar a função built-in pow()
        lista_saida.append(pow(numero, 2))

    # Podemos fazer utilizando list comprehension
    # lista_saida = [pow(numero, 2) for numero in lista_de_numeros]

    return lista_saida

if __name__ == '__main__':

    lista_de_numeros = [9, 4, 2, 3, 7]
    print(f"Lista de entrada: {lista_de_numeros}")
    print(f"Lista dos quadrados: {exercicio_04(lista_de_numeros)}")
