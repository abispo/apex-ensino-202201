
if __name__ == '__main__':

    _file = open('clientes.txt', mode='r')

    # read(<bytes>)    -> Lê o conteúdo do arquivo. O argumento bytes indica a quantidade de caracteres
    # que queremos ler

    texto = _file.read()
    # texto = _file.read(10) Lê os primeiros 10 caracteres

    _file.close()       # Sempre devemos fechar o arquivo que abrimos

    _file = open('clientes.txt', mode='r')

    # readline()    -> Lê uma linha por vez
    print(_file.readline())
    print(_file.readline())

    _file.close()

    _file = open('clientes.txt', mode='r')

    # readlines()   -> Lê o arquivo e retorna todas as linhas como uma lista

    linhas = _file.readlines()

    print(linhas)