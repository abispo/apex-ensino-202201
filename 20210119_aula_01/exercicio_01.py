
if __name__ == '__main__':
    a = input("Digite a primeira nota: ")
    b = input("Digite a segunda nota: ")
    c = input("Digite a terceira nota: ")

    resultado = float(a) + float(b) + float(c)

    media = resultado / 3

    print(f"A média é de {media}")

    # if... elif... else

    # Se a média do aluno for maior ou igual a 7, mostrar mensagem "Você foi aprovado!"
    # Se a média do aluno for maior ou igual a 5 e menor que 7, mostrar mensagem "Você está de recuperação"
    # Se a média do aluno for menor que 5, mostrar "Você foi reprovado."

    if media >= 7:
        print("Você foi aprovado!")

    elif media >= 5 and media < 7:
        print("Você está de recuperação.")

    else:
        print("Você foi reprovado.")