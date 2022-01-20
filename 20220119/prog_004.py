# entrada e saída pelo terminal

# __name__ é uma variável interna do Python
if __name__ == '__main__':

    # Imprime no terminal a saída do comando
    print("Curso de Python.")

    # input() permite que capturemos uma entrada pelo terminal.
    nome = input("Digite o seu nome: ")
    print(f"{nome}, bem-vindo ao curso de Python.")

    # input() e print() são funções built-in da linguagem.

    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")
    resultado = int(numero_1) + int(numero_2)


    # O resultado abaixo será a concatenação dos valores de numero_1 e numero_2
    # Por padrão, a função input sempre retorna uma string, independentemente do que foi
    # inserido no terminal
    # Nesse caso, precisamos converter os valores para tipos numéricos antes de fazer a operação
    # No python, temos 3 tipos de dados numéricos:
    # int()     -> Números inteiros (sem casa decimal)
    # float()   -> Números que possuem casa decimal
    # complex() -> Números complexos    (3j)
    print(f"{numero_1} + {numero_2} = {resultado}")