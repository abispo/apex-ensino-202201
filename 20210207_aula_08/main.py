from database import session, engine, Base
from models import Product

if __name__ == '__main__':

    Base.metadata.create_all(engine)

    COMANDO_SAIR = False
    SAIR = 0
    CADASTRAR_PRODUTO = 1
    LISTAR_PRODUTOS = 2
    APAGAR_PRODUTO = 3
    ATUALIZAR_PRODUTO = 4

    MENSAGEM = f"""
    SAIR -> {SAIR}
    CADASTRAR NOVO PRODUTO -> {CADASTRAR_PRODUTO}
    LISTAR PRODUTOS -> {LISTAR_PRODUTOS}
    APAGAR UM PRODUTO -> {APAGAR_PRODUTO}
    ATUALIZAR UM PRODUTO -> {ATUALIZAR_PRODUTO}
    """

    while not COMANDO_SAIR:
        print(MENSAGEM)
        opcao = int(input("INFORME O QUE DESEJA FAZER: "))

        if opcao == SAIR:
            COMANDO_SAIR = True
            continue

        elif opcao == CADASTRAR_PRODUTO:
            name = input("INFORME O NOME DO PRODUTO: ")
            price = float(input("INFORME O PREÇO DO PRODUTO: "))

            # Primeiro instanciamos o objeto Product usando os valores que foram passados via linha de comando
            product = Product(name=name, price=price)

            # Após isso, adicionamos o objeto Product a sessão do banco de dados
            session.add(product)

            # Por fim, damos commit no comando, ou seja, ele é executado no banco de dados
            session.commit()

            print(f"PRODUTO {product.name} CADASTRADO COM SUCESSO!")

        elif opcao == LISTAR_PRODUTOS:
            all_products = session.query(Product).all()

            MENSAGEM = "== LISTA DE PRODUTOS =="
            print(MENSAGEM)
            for product in all_products:
                TEXTO_PRODUTO = f"""
                ID: {product.id}
                NAME: {product.name}
                PRICE: {product.price:.2f}
                """

                print(TEXTO_PRODUTO)

            continue

        elif opcao == APAGAR_PRODUTO:
            product_id = int(input("INFORME O ID DO PRODUTO A SER APAGADO: "))

            product = session.query(Product).get(product_id)

            if not product:
                print(F"O PRODUTO DE ID {product_id} NÃO EXISTE!")
            else:
                session.delete(product)
                session.commit()

        elif opcao == ATUALIZAR_PRODUTO:
            product_id = int(input("INFORME O ID DO PRODUTO A SER ATUALIZADO: "))

            product = session.query(Product).get(product_id)

            if not product:
                print(F"O PRODUTO DE ID {product_id} NÃO EXISTE!")
            else:
                new_name = input("INFORME O NOVO NOME DO PRODUTO (DEIXE EM BRANCO PARA MANTER): ")
                new_price = float(input("INFORME O NOVO PREÇO DO PRODUTO (DEIXE EM BRANCO PARA MANTER): "))

                product.name = new_name if new_name else product.name
                product.price = new_price if new_price else product.name

                session.commit()
