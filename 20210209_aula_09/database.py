import os

# Importa a função que irá criar o objeto de conexão ao banco de dados
from sqlalchemy import create_engine

# Importa a função que irá criar o objeto de sessão, que vai enviar comandos ao banco de dados
from sqlalchemy.orm import sessionmaker

# Importa a função que irá criar classe base em que todas as classes que serão mapeadas para tabelas no
# banco de dados devem herdar.
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DATABASE_USER')
DB_HOST = os.getenv('DATABASE_HOST')
DB_PASS = os.getenv('DATABASE_PASSWD')
DB_NAME = os.getenv('DATABASE_NAME')

connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# create_engine retorna um objeto engine, que é o responsável por estabelecer a conexão com o banco de dados
# engine=True vai imprimir no terminal os comandos SQL que serão executados
engine = create_engine(connection_string, echo=False)

# declarative_base retorna a classe base de onde todas as classes que serão mapeadas para tabelas
# devem herdar.
Base = declarative_base()


Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    print(connection_string)