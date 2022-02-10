# Exercício 01
# Escreva uma função que receba 4 argumentos: nome, nota_1, nota_2, nota_3
# A função vai tirar a média das 3 notas, e mostrar o valor junto com o nome do Aluno:
# Se a média ficou abaixo de 5, o aluno foi reprovado
# Se a média ficou entre 5 e 6.9, o aluno está de recuperação
# Se a média ficou maior ou igual a 7, o aluno foi aprovado.

def mostrar_media(nome_aluno, nota_1, nota_2, nota_3):

    soma_das_notas = nota_1 + nota_2 + nota_3
    media = soma_das_notas / 3

    if media < 5:
        mensagem = "REPROVADO!"
    elif media >= 5 and media < 7:
        mensagem = "RECUPERACAO!"
    else:
        mensagem = "APROVADO!"

    print(f"Aluno: {nome_aluno}.")
    print(f"Média: {media:.2f}.")
    print(f"Situação: {mensagem}")
    print('-'*60)


if __name__ == '__main__':
    mostrar_media('Ana', 8, 9, 10)
    mostrar_media('Carlos', 6, 5, 7)
    mostrar_media('Antônio', 5, 4, 5)