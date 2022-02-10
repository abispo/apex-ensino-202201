# Função é um block de código que pode ser chamada sempre que precisarmos que ele rode
# Funções podem receber dados, na forma de argumentos/parâmetros
# Funções podem ou não retornar um valor

from random import randint

# A sintaxe de criação de funções em Python é a seguinte:
def hello():
    print(f"Olá mundo.{pow(randint(1, 100), 2)}")


# nome pode tanto ser chamada de argumento como de parâmetro
def bemvindo(nome):
    print(f"Bem vindo {nome}")


# uma função pode receber qualquer quantidade de argumentos
def soma(numero_1, numero_2):
    print(f"A soma de {numero_1} + {numero_2} é igual a {numero_1+numero_2}")


def minha_cidade(nome, cidade='Blumenau'):
    print(f"Olá! meu nome é {nome} e sou de {cidade}")


# Argumentos arbitrários
# Quando não sabemos exatamente quantos argumentos serão passados para a função, utilizamos um asterisco
# antes do nome do parâmetro na definição da função

# ingredientes(lista)
def ingredientes(*args):
    for arg in args:
        print(arg)


def resumo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def media(*args):
    # sum() e len() são 2 funções built-in do Python

    media = sum(args) / len(args)
    return media


if __name__ == '__main__':

    hello()
    bemvindo('João')
    soma(10, 5)
    soma(numero_2=1, numero_1=2)
    minha_cidade('Osasco', 'José')

    # Podemos usar parâmetros nomeados para ignorar a ordem dos argumentos
    minha_cidade(cidade='Blumenau', nome='Hans')

    minha_cidade('Maria')
    minha_cidade('Marta', cidade='Pomerode')

    # Exercício 01

    ingredientes("Pimenta", "Cebolinha", "Pimenta do Reino")

    usuario = {
        'nome': 'José da Silva',
        'idade': 41,
        'gênero': 'M',
        'setor': 'Financeiro'
    }

    resumo(**usuario)

    print(media(6, 5, 8))
