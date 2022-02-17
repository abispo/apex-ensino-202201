from database import session
from models import User


if __name__ == '__main__':


    user_email = input("INFORME O E-MAIL DO USUÁRIO PARA OBTER INFORMAÇÕES: ")

    user = session.query(User).filter(User.email == user_email).first()
    # SELECT * FROM tb_users WHERE email = 'non.leo@outlook.ca'

    # SELECT * FROM tb_users WHERE idade > 30 AND pais = "Brasil" LIMIT 1
    # users = session.query(User).filter(User.idade == 30, User.pais == "Brasil").first()

    if not user:
        print(f"O USUÁRIO DE E-MAIL {user_email} NÃO FOI LOCALIZADO NA BASE DE DADOS.")

    else:
        all_user_orders = user.orders

        if len(all_user_orders) == 0:
            print("ESSE USUÁRIO NÃO POSSUI PEDIDOS.")

        else:
            for user_order in all_user_orders:
                print(f"ITENS DO PEDIDO NUMERO {user_order.id}:")
                for order_product in user_order.products:
                    print(f"* {order_product.name}")