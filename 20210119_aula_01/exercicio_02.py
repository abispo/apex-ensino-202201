# Exercício 2
# Escreva uma rotina que receba a altura e o peso de uma pessoa, e com essas informações faça o cálculo
# do IMC. A fórmula para cálculo do IMC de uma pessoa é a seguinte: IMC = peso / (altura * altura). Após isso, indicar
# Se a pessoa está obesa ou não seguindo as regras abaixo:
# IMC menor que 18.5 -> Pessoa com baixo peso
# IMC maior ou igual a 18.5 e menor que 25 -> Pessoa com peso adequado
# IMC maior ou igual a 25 e menor que 30 -> Pessoa com sobrepeso
# IMC maior ou igual a 30 -> Pessoa com obesidade

if __name__ == '__main__':

    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = peso / (altura * altura)

    # Para formatar a quantidade de casas decimais exibidas, usamos a seguinte regra:
    # .2f (2 casas decimais depois do ponto#
    print(f"Seu IMC é de {imc:.2f}")

    if imc < 18.5:
        print("Você está com baixo peso.")
    elif imc >= 18.5 and imc < 25:
        print("Você está com o peso ideal.")
    elif imc >= 25 and imc < 30:
        print("Você está com sobrepeso.")
    else:
        print("Você está com obesidade.")