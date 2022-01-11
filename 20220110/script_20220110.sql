# 20220110

# Esse é um comentário
/* Esse é um comentário */
-- Esse é outro comentário

# BANCO DE DADOS - AULA -1

/*
Banco de dados pode ser entendido como uma coleção de dados que são 
armazenados e acessados eletronicamente. Um banco de dados permite 
não apenas a captura desses dados armazenados,
mas também a alteração, inserção e remoção de dados. 
Um simples arquivo de texto pode ser entendido como um banco de dados.

- Um sistema gerenciador de banco de dados (SGBD) é um sistema que 
interage com os usuários, applicações e o próprio banco de dados em 
si para capturar e analisar os dados.

- Existem diferentes tipos de banco de dados, tais como:
	- Banco de dados Relacional
    - Banco de dados NoSQL
    - Banco de dados Chave-Valor
    
- SQL -> Structured Query Language - Linguagem de Consulta Estruturada

- DDL: Data Definition Language     -> CREATE, ALTER, DROP
- DML: Data Manipulation Language   -> INSERT, UPDATE, DELETE (SELECT)
	- DQL: Data Query Language      -> SELECT
- DTL: Data Transaction Language    -> START TRANSACTION, COMMIT, ROLLBACK
- DCL: Data Control Language        -> GRANT, REVOKE
*/

# Criando um banco de dados
# NÃO ESQUEÇA DO PONTO-E-VÍRGULA NO FINAL
CREATE DATABASE aula_20220110;

# Definindo o banco aula_20220110 como padrão
USE aula_20220110;

# Criando tabelas
# Uma tabela no banco de dados é formada por colunas e linhas
# Cada coluna deve ter um tipo de dado.
CREATE TABLE tb_clients (
	# A coluna 'id' será do tipo INT (numérico) e não pode conter valores nulos.
	id INT NOT NULL,
    
    # A coluna 'name' será do tipo texto (string) variável e não pode conter valores nulos
    name VARCHAR(100) NOT NULL,
    
   # A coluna 'gender' será do tipo texto (string) e não pode conter valores nulos
    gender CHAR(10) NOT NULL,
    
	# A coluna 'birth_date' será do tipo data e pode conter valores nulos
    birth_date DATE NULL
);

# O comando DESC mostra a estrutura da tabela
# Pode ser usada a forma curta 'DESC'
DESCRIBE clients;

# Utilizamos o ALTER quando queremos fazer alguma modificação em uma tabela
# Vamos inserir uma nova coluna (ADD)
ALTER TABLE tb_clients ADD score INT NOT NULL;

# Vamos modificar o tipo de dado da coluna
ALTER TABLE tb_clients MODIFY score CHAR(1) NOT NULL;

# Vamos modificar o nome da tabela
ALTER TABLE tb_clients RENAME TO clients;

# Vamos apagar a tabela;
DROP TABLE clients;

# SQL é uma linguagem case-insensitive
# ou seja, não diferencia letras maiúsculas e minúsculas
CREATE TABLE alunos(
	nome VARCHAR(100) NOT NULL,
    nota_1 INT NOT NULL,
    nota_2 INT NOT NULL,
    nota_3 INT NOT NULL
);

# Inserindo dados na tabela
INSERT INTO alunos(nome, nota_1, nota_2, nota_3) VALUES ('Maria', '3', 5, 6);
# Cast -> Conversão de tipo

# Consultamos os dados da tabela utilizando o comando SELECT
# O asterisco indica que queremos trazer todos os registros de todas as colunas
SELECT * FROM alunos;

# Se quisermos apenas algumas colunas, devemos especificá-las
SELECT nome, nota_2 FROM alunos;

# Inserindo novos registros
# Podemos inserir várias linhas dentro de um INSERT utilizando a sintaxe abaixo:
INSERT INTO alunos(nome, nota_1, nota_2, nota_3) VALUES
	('João', 6, 7, 9),
    ('Roberto', 9, 9, 10),
    ('Amanda', 10, 10, 9),
    ('Julia', 7, 7, 9);
    
SELECT * FROM alunos;

# Quando queremos atualizar uma informação, utilizamos o comando UPDATE;

UPDATE alunos SET nota_1 = 9;

# O MySQL Workbench trava por padrão os comandos UPDATE e DELETE. Temos que
# liberar manualmente
SET SQL_SAFE_UPDATES=0;

# Utilizamos a cláusula WHERE quando queremos modificar os registros apenas
# quando uma determinada condição é satisfeita;

UPDATE alunos SET nota_1 = 8 WHERE nome = 'João' AND nota_2 > 10;

SELECT * FROM alunos;

# Utilizamos o comando DELETE para apagar registros da tabela
# DELETE FROM alunos; # TODOS OS REGISTROS SERÃO APAGADOS!!!

DELETE FROM alunos WHERE nome = 'Julia';

/*
	Criar uma tabela de produtos com as seguintes colunas:
		- id INT NOT NULL
        - nome VARCHAR(100)
        - preco FLOAT

	Vão inserir 5 produtos
    Depois vão atualizar o valor de 1 produto
    Após isso, vão apagar 2 produtos (deve ser feito em 1 comando)
*/

# Criar a tabela
# A cláusula IF NOT EXISTS diz ao banco para verificar se a tabela que
# está sendo criada já existe. Se existir, é mostrado um aviso.
CREATE TABLE IF NOT EXISTS produtos(
	id INT NOT NULL,
    nome VARCHAR(100),
    preco FLOAT
);

SELECT * FROM produtos; 

# No MySQL, utilizamos o ponto (.) para separar as casas decimais dos valores
# FLOAT e DOUBLE
INSERT INTO produtos (id, nome, preco) VALUES
	(1, 'Shampoo', 9.90),
    (2, 'Detergente', 4.45),
    (3, 'Sabão', 2.90),
    (4, 'Esfregão', 11),
    (5, 'Sabonete', 1.50);
    
# Atualizar o valor de 1 produto
UPDATE produtos SET preco = 10.45 WHERE nome = 'Esfregão';

# Apagar 2 produtos
DELETE FROM produtos WHERE id = 3 OR id = 4;
