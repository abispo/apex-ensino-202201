import csv

from models import User, Profile, Product, Order, orders_products
from database import session, engine

if __name__ == '__main__':

    all_users = session.query(User).all()

    if len(all_users) > 0:
        print("OS DADOS DA tb_users JÁ FORAM CARREGADOS")
    else:
        filename = "users.csv"
        print(f"CARREGANDO OS DADOS DO ARQUIVO {filename}")

        with open(filename, mode='r') as _file:
            reader = csv.DictReader(_file, delimiter=';')

            for line in reader:
                user = User(email=line.get('email'), passwd=line.get('passwd'))

                # Podemos também desempacotar (unpacking) o dicionário no método construtor da class
                # user = User(**line)
                session.add(user)
                session.commit()

    all_profiles = session.query(Profile).all()

    if len(all_profiles) > 0:
        print("OS DADOS DA tb_profiles JÁ FORAM CARREGADOS")
    else:
        filename = "profiles.csv"
        print(f"CARREGANDO OS DADOS DO ARQUIVO {filename}")

        with open(filename, mode='r') as _file:
            reader = csv.DictReader(_file, delimiter=";")

            for line in reader:
                profile = Profile(**line)

                session.add(profile)
                session.commit()

    all_products = session.query(Product).all()

    if len(all_products) > 0:
        print("OS DADOS DA tb_products JÁ FORAM CARREGADOS")

    else:
        filename = "products.csv"

        with open(filename, mode="r") as _file:
            reader = csv.DictReader(_file, delimiter=";")

            for line in reader:
                product = Product(**line)

                session.add(product)
                session.commit()

    all_orders = session.query(Order).all()

    if len(all_orders) > 0:
        print("OS DADOS DA tb_orders JÁ FORAM CARREGADOS")

    else:
        filename = "orders.csv"

        with open(filename, mode="r") as _file:
            reader = csv.DictReader(_file, delimiter=";")

            for line in reader:
                order = Order(**line)

                session.add(order)
                session.commit()

    all_orders_products = engine.execute(orders_products.select()).all()

    if len(all_orders_products) == 0:
        filename = "orders_products.csv"

        with open(filename, mode="r") as _file:
            reader = csv.DictReader(_file, delimiter=";")

            for line in reader:
                insert_table = orders_products.insert().values(**line)
                engine.execute(insert_table)
