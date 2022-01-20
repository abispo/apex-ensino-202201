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

    # Exercício 1
    # Criar uma rotina que receba 3 notas (a, b, c)
    # Calcular a média das notas e imprimir no console (a + b + c / 3 )
    # Se a média for maior ou igual a 7, imprimir a mensagem "Você foi aprovado."

    # Exercício 2
    # Escreva uma rotina que receba a altura e o peso de uma pessoa, e com essas informações faça o cálculo
    # do IMC. A fórmula para cálculo do IMC de uma pessoa é a seguinte: IMC = peso / (altura * 2). Após isso, indicar
    # Se a pessoa está obesa ou não seguindo as regras abaixo:
    # IMC menor que 18.5 -> Pessoa com baixo peso
    # IMC maior ou igual a 18.5 e menor que 25 -> Pessoa com peso adequado
    # IMC maior ou igual a 25 e menor que 30 -> Pessoa com sobrepeso
    # IMC maior ou igual a 30 -> Pessoa com obesidade