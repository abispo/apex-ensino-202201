
def exercicio_03(lista):
    lista.sort(reverse=True)
    return lista[0]


if __name__ == '__main__':
    lista = [5, 5, 6, 6, 2, 7]
    print(f"Maior número: {exercicio_03(lista)}")
