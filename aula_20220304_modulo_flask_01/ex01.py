from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

# Exercício
# Rodar pelo terminal: FLASK_ENV=development python main.py
# Rodar pelo PyCharm: Adicionar a variável de ambient FLASK_ENV=development na configuração
# de execução

# Criar uma API de cadastro de clientes
# Os dados armazenados serão:
# - id (uuid4), nome, email

# Criar 3 endpoints:
# - /users -> Vai cadastrar os dados (POST)
# - /users -> Vai listar todos os usuários (GET)
# - /users/<id> -> Vai listar um usuário em específico, pelo ID (GET)

# Os dados deverão ser armazenados em uma lista
users_list = []

# Estrutura:
# [
#   {id': '0dcb8fba-f01d-46e1-87ea-72116e2db478', 'nome': 'Maria', 'email': 'maria@email.com'}
#   {id': '17655861-bcf5-4492-befb-a65aaca57967', 'nome': 'Paulo', 'email': 'paulo@email.com'}
# ]

if __name__ == '__main__':
    app.run()
