
from flask import Flask, request, jsonify
from http import HTTPStatus
from datetime import datetime

# Precisamos criar o objeto Flask que vai representar a nossa aplicação
app = Flask(__name__)


# Dessa maneira criamos as rotas (ou endpoints) na nossa aplicação.
@app.route('/')
@app.route('/index')
def index():
    return "Hello World"


# Quando queremos passar um argumento na rota (url), utilizamos a sintaxe <<tipo:>argumento>
# Quando não especificamos o tipo, o argumento é passado como string
# Esse argumento deve ser passado também para a função.
@app.route('/hello/<username>')
def hello_username(username):
    return f"Hello {username}!"


@app.route('/quadrado/<int:numero>')
def quadrado(numero):
    return f"O quadrado de {numero} é {numero * numero}"


@app.route('/datenow', methods=['GET'])
def datenow():
    return datetime.now().strftime("%H:%M:%S %Y-%m-%d")

# {
#     'number_1': 10,
#     'number_2': 20,
#     'operation': '+'
# }


@app.route('/users', methods=['POST'])
def create_user():
    pass


@app.route('/users', methods=['GET'])
def get_all_users():
    pass


@app.route('/operation', methods=['POST'])
def operation():
    data = request.json


    operation = data.get('operation')
    number_1 = int(data.get('number_1'))
    number_2 = int(data.get('number_2'))

    if operation == '+':
        result = number_1 + number_2

    elif operation == '-':
        result = number_1 - number_2

    elif operation == '*':
        result = number_1 * number_2

    elif operation == '/':
        result = number_1 / number_2

    else:
        return jsonify(message="Operação desconhecida"), HTTPStatus.NOT_FOUND

    return jsonify(result=result), HTTPStatus.OK



if __name__ == '__main__':
    app.run()

