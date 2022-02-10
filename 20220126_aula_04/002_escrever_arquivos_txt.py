
if __name__ == '__main__':

    #_file = open('clientes.txt', mode='w')

    # write()   -> Escreve um conteúdo no arquivo
    # _file.write('Daniela')

    #_file.close()

    #_file = open('clientes.txt', mode='w')

    # writelines()      -> Recebe uma lista de valores e escreve no arquivo
    #_file.writelines(['Banana\n', 'Mexerica\n', 'Coco\n'])

    #print(_file.closed)

    #_file.close()

    with open('clientes.txt', mode='r') as _file:
        print(_file.closed)
        print(_file.read())

    print(_file.closed)

