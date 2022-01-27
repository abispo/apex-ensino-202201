# CSV   -> Comma Separated Values
import csv


def info_curso(codigo, nome, valor):
    print(f"Código do curso: {codigo}")
    print(f"Nome do curso: {nome}")
    print(f"Valor do curso: {valor}")
    print('-' * 50)

if __name__ == '__main__':

    with open("cursos.csv", mode='r') as _file:

        # Maneira 'comum' utilizando csv.reader
        reader = csv.reader(_file, delimiter=';')

        print("LISTA DE CURSOS")
        print("")

        for line in reader:
            info_curso(*line)


    # Utilizando DictReader
    with open("cursos.csv", mode='r') as _file:
        reader = csv.DictReader(_file, delimiter=';')

        for line in reader:
            info_curso(**line)