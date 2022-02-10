
def exercicio_08(**kwargs):
    print(len(kwargs))
    print(kwargs)

def exercicio_08_a(nome, idade, genero):
    print(f"Nome: {nome} | Idade: {idade} | Gênero: {genero}")

if __name__ == '__main__':

    pessoa = {
        'nome': 'Maria',
        'idade': 29,
        'genero': 'F'
    }

    exercicio_08(**pessoa)
    exercicio_08_a(**pessoa)
