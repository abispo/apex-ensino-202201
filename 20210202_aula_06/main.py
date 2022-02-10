import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor(buffered=True)

if __name__ == '__main__':

    database_name = "aula_20220202"

    print("Iniciando...")

    comando = f"CREATE DATABASE IF NOT EXISTS {database_name}"

    cursor.execute(comando)

    comando = f"USE {database_name}"
    cursor.execute(comando)

    # User.objects.all()
    # SELECT * FROM users;

    comando = """
    CREATE TABLE IF NOT EXISTS tb_users(
        id INT NOT NULL AUTO_INCREMENT,
        username VARCHAR(200) NOT NULL,
        email VARCHAR(200) NOT NULL,
        birth_date DATE NOT NULL,
        PRIMARY KEY(id)
    )
    """

    cursor.execute(comando)

    print("CADASTRO DE USUÁRIOS")

    SAIR = False
    LISTAR = 1
    INSERIR = 2
    APAGAR = 3

    while not SAIR:
        opcao = int(input("Digite a opção (1 -> Listar | 2 -> Inserir | 3 -> Apagar | 0 -> Sair: "))

        if opcao == 0:
            SAIR = True

        elif opcao == LISTAR:
            comando = "SELECT * FROM tb_users"
            cursor.execute(comando)

            users = cursor.fetchall()

            if cursor.rowcount > 0:
                for user in users:
                    saida = f"""
                    username: {user[1]}
                    email: {user[2]}
                    data de nascimento: {user[3]}
                    """
                    print(saida)
            else:
                print("NÃO EXISTEM USUÁRIOS CADASTRADOS.")

        elif opcao == INSERIR:
            print("INFORME OS DADOS DO USUÁRIO")
            username = input("Informe o username: ")
            email = input("Informe o e-mail: ")
            birth_date = input("Informe a data de nascimento no formato indicado (YYYY-MM-DD): ")

            comando = f"""
            INSERT INTO tb_users(username, email, birth_date) VALUES ('{username}', '{email}', '{birth_date}')
            """

            cursor.execute(comando)
            db.commit()

            if cursor.rowcount > 0:
                print("USUÁRIO SALVO COM SUCESSO")

            else:
                print("HOUVE ALGUM ERRO!")

        elif opcao == APAGAR:
            user_id = int(input("INFORME O ID DO USUÁRIO QUE PRETENDE APAGAR: "))

            comando = f"SELECT * FROM tb_users WHERE id = '{user_id}'"

            cursor.execute(comando)

            if cursor.rowcount == 0:
                print(f"O USUÁRIO DE ID {user_id} NÃO EXISTE!")

            else:
                user = cursor.fetchone()

                comando = f"DELETE FROM tb_users WHERE id = {user_id}"
                cursor.execute(comando)
                db.commit()

                print(f"O usuário {user[2]} foi excluído")