# Crie uma rotina que receba 5 números pelo terminal, e no final faça a soma desses números. Use
# o laço for pra pegar esses números

if __name__ == '__main__':

    soma_total = 0

    for i in range(5):
        numero = int(input("Digite um número: "))
        soma_total = soma_total + numero
        # soma_total += numero  # Faz a mesma coisa que a linha acima mas de maneira resumida

    print(f"A soma total dos números é de {soma_total}")
