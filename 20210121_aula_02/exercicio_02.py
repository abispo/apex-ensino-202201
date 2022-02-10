# Receba pelo terminal um texto qualquer e o imprima. Se o texto digitado for "sair", o programa encerra.
# Utilize o laço while para isso

if __name__ == '__main__':

    texto = ''

    while texto != 'sair':
        texto = input("Digite um texto: ")
        print(texto)
