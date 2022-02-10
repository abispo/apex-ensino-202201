
def calculo_salario(nome, valor, setor, horas_trabalhadas=0, porcentagem_comissao=0):

    print("-"*50)
    print(f"Cálculo do salário de {nome}")

    if setor == 1:
        print(f"Salário: {valor:.2f}")

    elif setor == 2:
        print(f"Quantidade de horas trabalhadas: {horas_trabalhadas}")
        print(f"Valor da hora trabalhada: {valor}")
        print(f"Salário: {valor * horas_trabalhadas:.2f}")

    elif setor == 3:
        print(f"Valor total das vendas: {valor}")
        print(f"Porcentagem de comissão: {porcentagem_comissao}%")
        print(f"Salário: {valor * (porcentagem_comissao / 100):.2f}")


if __name__ == '__main__':

    nome = input("Digite o nome do funcionário: ")
    valor = float(input("Digite o valor: "))
    setor = int(input("Digite o setor: "))

    if setor == 1:
        calculo_salario(nome, valor, setor)

    elif setor == 2:
        qtd_horas = int(input("Informe a quantidade de horas trabalhadas: "))
        calculo_salario(nome, valor, setor, horas_trabalhadas=qtd_horas)

    elif setor == 3:
        porcentagem_comissao = int(input("Informe a porcentagem de comissão: "))
        calculo_salario(nome, valor, setor, porcentagem_comissao=porcentagem_comissao)

    else:
        print("Esse setor não existe.")

