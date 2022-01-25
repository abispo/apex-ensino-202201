
# O laço while executa um bloco de código enquanto uma condição for verdadeira.

if __name__ == '__main__':

    i = 0

    while i > 10:
        print(i)

        i = i + 1

    # Assim como no laço for, podemos utilizar o else no laço while
    else:
        print("Loop finalizado")

    print("Finalizado!")

    i = 0

    # Assim como no laço for, podemos controlar o fluxo de execução do laço while utilizando break/continue
    while i < 10:
        if i == 5:
            print("5 não é permitido")
            break
        print(i)
        i = i + 1

    i = 0

    while i < 10:
        if i == 5:
            i += 1
            continue

        print(i)
        i += 1

    # Exercício 2