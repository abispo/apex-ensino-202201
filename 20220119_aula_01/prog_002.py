
# Isso é um comentário

if __name__ == '__main__':

    # 1. A linguagem Python é *case sensitive*, ou seja, distingue letras maiúsculas e minúsculas. Exemplo:
    print('1')
    nome_funcionario = "John"

    print(nome_funcionario)

    # 2. Não usamos ; ou qualquer outro caractere pra indicar o término de um comando. O próprio final de
    # linha indica que o comando terminou
    print("\n2")        # \n significa pule uma linha
    print("Esse é um comando.")
    print("Esse é outro comando.")

    # 3. Caso deseje utilizar mais de 1 comando (statement) por linha, aí sim utilizamos ;
    print("\n3"); nome = "Flávia"; print(nome)

    # 4. Podemos definir strings multi linhas utilizando 3 strings consecutivas (''', """)
    print("\n4")
    texto_multi_linha = '''
        1. Primeiro parágrafo
            2. Segundo parágrafo
            
            Lorem ipsum alguma coisa
    
    '''

    print(texto_multi_linha)

    # 5. Se quisermos definir um comando multilinha, usamos o caractere \ (barra invertida). Valores dentro de
    # (), [], {} não precisam desse caractere especial.

    print("\n5")
    calculo = 4 + 5 * (2 / 2) + 8 * \
        (4 + 4) * 50 / 10 - \
              8 + 2

    print(calculo)

    # 6. Python usa identação de código em suas regras de sintaxe. Em comparação, linguagens como Java, C,
    # PHP, etc utilizam {} pra definir blocos de código. Por exemplo:

    comandos_javascript = """
    if (condicao) { variavel = true; } else {
        variavel = false;
    }
    """

    print("\n6")

    usuario = "Maria"

    if usuario == "Maria":
    # print("Essa linha causa erro.")
        print("O usuário é " + usuario)

    usuario = "João"

    if usuario == "João":
        print("João logou...")

            #print("Essa linha causa erro")

        print("Bem vindo João")

        valor = 10

        if valor == 10:
            print("Seu valor é 10")
            print("Ok.")

    # Definimos um bloco de código depois que usamos o caractere : nos casos:
    # Bloco de condição
    # Bloco de repetição
    # Definição de função
    # Definição de classes e métodos
    # Criação de contexto com with
