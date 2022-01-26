from random import randint


def exercicio_05(lista_de_numeros):
    lista_de_numeros_impares = []
    for numero in lista_de_numeros:
        if numero % 2 == 1:
            lista_de_numeros_impares.append(numero)

    return lista_de_numeros_impares


if __name__ == '__main__':

    # list comprehension que cria uma lista de números de forma randômica
    lista_de_numeros = [randint(1, 50) for _ in range(10)]
    lista_de_numeros_impares = exercicio_05(lista_de_numeros)

    print(f"Lista de números de entrada: {lista_de_numeros}")
    print(f"Lista de números ímpares: {lista_de_numeros_impares}")



