
def exercicio_07(*args):
    print(f"Quantidade de argumentos: {len(args)}")
    print(f"Valor dos argumentos: {args}")


if __name__ == '__main__':

    exercicio_07(1, 2, 3, 5, 6, 5, 3)
    lista = [1, 5, 6, 4, 5]
    exercicio_07(*lista)    # unpacking de argumentos
