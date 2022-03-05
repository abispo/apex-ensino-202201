from http import HTTPStatus

from flask import Flask, request, jsonify
from uuid import uuid4

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

# Estrutura:
# [
#   {id': '0dcb8fba-f01d-46e1-87ea-72116e2db478', 'nome': 'Maria', 'email': 'maria@email.com'}
#   {id': '17655861-bcf5-4492-befb-a65aaca57967', 'nome': 'Paulo', 'email': 'paulo@email.com'}
# ]

app = Flask(__name__)
users_list = []


@app.route("/users", methods=['POST'])
def create_user():
    data = request.json
    id = str(uuid4())
    data['id'] = id

    users_list.append(data)

    return data, HTTPStatus.CREATED


@app.route("/users", methods=['GET'])
def get_all_users():
    return jsonify(users_list), HTTPStatus.OK


@app.route("/users/<id>", methods=['GET'])
def get_user(id):
    for user in users_list:
        if user.get('id') == id:
            return jsonify(user), HTTPStatus.OK

    return "", HTTPStatus.NOT_FOUND


@app.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    for user in users_list:
        if user.get('id') == id:
            users_list.remove(user)
            return "", HTTPStatus.NO_CONTENT

    return "", HTTPStatus.NOT_FOUND

if __name__ == '__main__':
    app.run()
