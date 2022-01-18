
/*
 * Funções de agregação
 * 		Funções de agrupamento são aplicadas em um conjunto de linhas para retornar um resultado por conjunto.
 * 		Exemplos de funções:
        AVG(), COUNT(), MAX(), MIN(), SUM().
*/

SELECT * FROM customers c ;

/* Retorna a quantidade total de clientes */
SELECT count(*) FROM customers c;

/*
	A cláusula GROUP BY agrupa linhas que possuem os mesmos valores em linhas sumarizadas.
*/
# alias -> apelido
SELECT country, count(*) Total FROM customers c GROUP BY country ORDER BY Total DESC ;

/* Se quisermos saber a quantidade total de linhas que foram agregadas, utilizamos a cláusula
 * WITH ROLLUP
 */

SELECT * FROM orderdetails o ;

# O comando abaixo mostra a quantidade de itens que foram solicitados por pedido
# A cláusula WITH ROLLUP gera uma linha final com a soma das colunas que foram agregadas
SELECT orderNumber, sum(quantityOrdered) AS totalItensOrdered
FROM orderdetails o
GROUP BY orderNumber WITH ROLLUP ;

/* EXERCÍCIOS */
/* 1) Escreva uma consulta que mostre a quantidade de funcionários por escritório (tabela employees), 
 * ordenando do maior para o menor
 * 
 * 2) Escreva uma consulta que retorne a quantidade de pedidos para cada status, e no final mostre a 
 * quantidade total de pedidos (tabela orders)
 */

SELECT * FROM employees e ;

# 1)
SELECT officeCode, count(employeeNumber) AS total FROM employees e GROUP BY officeCode ORDER BY total DESC ;

# 2)
SELECT status, count(orderNumber) FROM orders o GROUP BY status WITH ROLLUP ;

# ----------------------------------------------------------------------------------------

CREATE DATABASE aula_20220114;
USE aula_20220114;

/* Chaves primárias

No modelo de bases de dados relacionais, utilizamos a chave primária quando queremos que uma quantidade determinada de 
colunas sirva como um identificador único para cada linha da tabela. Ou seja, utilizando chave primária podemos identificar 
unicamente um registro, garantindo que não haja valores repetidos desse identificador.
*/

CREATE TABLE tb_clientes(
	id INT,
	nome VARCHAR(100)
);

INSERT INTO tb_clientes (id, nome) VALUES (1, 'Maria');
INSERT INTO tb_clientes (id, nome) VALUES (2, 'José');
INSERT INTO tb_clientes (id, nome) VALUES (3, 'Luana');

SELECT * FROM tb_clientes;

INSERT INTO tb_clientes (id, nome) VALUES (1, 'Paulo');
INSERT INTO	tb_clientes (nome) VALUES ('Amanda');

DROP TABLE tb_clientes;

CREATE TABLE tb_clientes(
	id INT NOT NULL,
	nome VARCHAR(100),
	PRIMARY KEY(id)
);

INSERT INTO tb_clientes (id, nome) VALUES (1, 'Maria');
INSERT INTO tb_clientes (id, nome) VALUES (2, 'José');
INSERT INTO tb_clientes (id, nome) VALUES (3, 'Luana');

SELECT * FROM tb_clientes;

INSERT INTO tb_clientes (id, nome) VALUES (1, 'Paulo');
INSERT INTO tb_clientes (id, nome) VALUES (4, 'Suzana');


/* Caso a tabela seja criada sem chave primária e desejamos adicioná-la depois, utilizamos ALTER TABLE */
/* ALTER TABLE tb_clientes ADD PRIMARY KEY (id) */

/* EXERCICIO */

/* Criar a tabela tb_pedidos com os seguintes campos:
 * 
 * Uma coluna id, deve ser do tipo inteiro, não permitir valores nulos e ser chave primária
 * Uma coluna descricao, deve ser do tipo varchar de tamanho 200, e não pode ter valores nulos
 *
 * Criar a tabela tb_servicos, que vai ter os seguintes campos:
 * Um coluna id, deve ser do tipo inteiro, não deve permitir valores nulos
 * Uma coluna descricao, deve ser do tipo varchar de tamanho 200, e não pode ter valores nulos

 * Após isso, a coluna id deve ser alterada para ser do tipo chave primária.
*/

# 1)
CREATE TABLE tb_pedidos(
	id INT NOT NULL,
	descricao VARCHAR(200) NOT NULL,
	PRIMARY KEY (id)
);

DESC tb_pedidos;

# 2)
CREATE TABLE tb_servicos(
	id INT NOT NULL,
	descricao VARCHAR(200) NOT NULL
);

ALTER TABLE tb_servicos ADD PRIMARY KEY (id);

DESC tb_servicos;

DROP TABLE tb_servicos;
DROP TABLE tb_clientes;

/* 
 * Podemos definir uma chave primária com o argumento AUTO_INCREMENT. Para tipos numéricos, esse argumento fará
 * com que o valor da coluna seja automaticamente incrementado sempre que houver novas inserções.
*/

CREATE TABLE tb_clientes(
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	PRIMARY KEY (id)
);

DESC tb_clientes;

INSERT INTO tb_clientes (nome) VALUES ('Maria');
INSERT INTO tb_clientes (nome) VALUES ('Marta');
INSERT INTO tb_clientes (nome) VALUES ('Daiane');
INSERT INTO tb_clientes (nome) VALUES ('Priscila');
INSERT INTO tb_clientes (nome) VALUES ('Barbara');

SELECT * FROM tb_clientes;

DROP TABLE tb_clientes;
DROP TABLE tb_pedidos;

# ---------------------------
/* NORMALIZAÇÃO DE TABELAS */

# Normalização é o processo de análise feito para assegurarmos que as relações entre as tabelas sejam bem formadas, 
# ou seja, que não gerem anomalias (inclusão, exclusão, alteração, etc)

# 1FN, 2FN, 3FN (FN -> Forma Normal)

CREATE TABLE tb_agencia_funcionarios(
	id_funcionario INT NOT NULL AUTO_INCREMENT,
	nome_funcionario VARCHAR(100) NOT NULL,
	numero_agencia INT NOT NULL,
	endereco_agencia VARCHAR(200) NOT NULL,
	PRIMARY KEY (id_funcionario)
);

INSERT INTO tb_agencia_funcionarios(nome_funcionario, numero_agencia, endereco_agencia) VALUES
	('José', 1001, 'Rua 2, 103'),
	('Maria', 1001, 'Rua 2, 103'),
	('Mario', 2003, 'Rua 5, 19'),
	('Paulo', 5456, 'Rua 46, 100'),
	('Valter', 1006, 'Rua 1, 17');

SELECT * FROM tb_agencia_funcionarios;

# Quando formos incluir um funcionário, corremos o risco de inserir um endereço diferente de uma mesma agência (anomalia de inclusão)
# Quando formos excluir um funcionário, os dados da agência também serão excluídos (anomalia de exclusão)
# Quando formos atualizar o endereço de uma agência, temos que atualizar pra todos os funcionários


/* O objetivo final da normalização de tabelas é chegar, pelo menos, na 3FN

/* 1FN -> Primeira Forma Normal */

/*
 * Reprovar atributos multivalorados
   O domínio de um atributo deve incluir apenas valores atômicos (indivisíveis)
   Uma tabela está na 1FN quando:
   	Somente possui valores atômicos(nível mais baixo de detalhamento)
   	Não há grupos de atributos repetidos
    Existe uma chave primária
    Relação não possui atributos multivalorados ou relações aninhadas(uma tabela dentro de outra tabela).
 */

CREATE TABLE tb_clientes(
	id INT NOT NULL,
	nome VARCHAR(200) NOT NULL,
	telefone VARCHAR(100) NOT NULL,
	endereco VARCHAR(200) NOT NULL
);

# 1) Definir o campo chave primária da tabela
ALTER TABLE tb_clientes ADD PRIMARY KEY (id);
ALTER TABLE tb_clientes MODIFY id INT NOT NULL AUTO_INCREMENT;
DESC tb_clientes;

INSERT INTO tb_clientes (nome, telefone, endereco) VALUES 
	('Paulo', '994560924', 'Rua treze de setembro, 1285, Jardim Flores, Blumenau, 89356204'),
	('Maria', '994560924, 923445519', 'Rua XV, 85, Jardim central, Indaial, 89122223'),
	('José', '994560924', 'Avenida angélica, 565, Centro, Gaspar, 89116901');

/*
 * Problemas identificados:
 * 	- O campo telefone possui mais de 1 valor
 *  - O campo endereco pode ser quebrado em outros campos
 */
	
SELECT * FROM tb_clientes;

/* Primeiro passo: Criar uma nova tabela que vai armazenar o(s) telefone(s) do clientes. */

CREATE TABLE tb_telefones(
	id INT NOT NULL AUTO_INCREMENT,
	id_cliente INT NOT NULL,
	telefone VARCHAR(20),
	PRIMARY KEY (id)
);

DESC tb_telefones;

INSERT INTO tb_telefones (id_cliente, telefone) VALUES (1, '5547981098732');
INSERT INTO tb_telefones (id_cliente, telefone) VALUES (2, '5547989023333');
INSERT INTO tb_telefones (id_cliente, telefone) VALUES (2, '5547909111132');

SELECT * FROM tb_telefones WHERE id_cliente = 2;

ALTER TABLE tb_clientes DROP COLUMN telefone;

# 2) Quebrar a coluna endereço em várias colunas, que vão possuir valores indivisiveis
ALTER TABLE tb_clientes ADD logradouro VARCHAR(20);
ALTER TABLE tb_clientes ADD nome_endereco VARCHAR(200);
ALTER TABLE tb_clientes ADD numero VARCHAR(10);
ALTER TABLE tb_clientes ADD bairro VARCHAR(100);
ALTER TABLE tb_clientes ADD cidade VARCHAR(100);
ALTER TABLE tb_clientes ADD cep VARCHAR(8);

ALTER TABLE tb_clientes DROP COLUMN endereco;

SELECT * FROM tb_clientes;

DROP TABLE tb_clientes;
DROP TABLE tb_telefones;

-----------------------
/* 2FN -> Segunda Forma normal
	A segunda forma normal se baseia NO conceito de dependência funcional total.
	Cada atributo que não FOR chave, tem que ser total e funcionalmente dependente da chave primária.
	
	Dizemos que uma tabela está na 2FN, quando:
		Está na 1FN
     	Todos os atributos não chave são funcionalmente dependentes de todas as partes da chave primária
      	Um atributo chave é um que é uma pk ou parte de uma pk composta
     	Não existem dependências parciais
     	Caso contrário, deve-se gerar uma nova tabela
*/

CREATE TABLE tb_vendas (
	id INT NOT NULL AUTO_INCREMENT,
	id_produto INT NOT NULL,
	nome_produto VARCHAR(200) NOT NULL,
	valor_produto FLOAT NOT NULL,
	quantidade INT NOT NULL,
	PRIMARY KEY (id, id_produto)
);

/*
 * Probleas identificados:
 * 	- as colunas nome_produto e valor_produto dependem apenas de parte da chave primária (id_produto)
 * 
 * Solução:
 * 	- Retirar essas colunas ta tb_vendas e colocar em uma nova tabela
 */

CREATE TABLE tb_vendas(
	id INT NOT NULL AUTO_INCREMENT,
	id_produto INT NOT NULL,
	quantidade INT NOT NULL,
	PRIMARY KEY (id, id_produto)
);

CREATE TABLE tb_produtos(
	id INT NOT NULL AUTO_INCREMENT,
	nome_produto VARCHAR(100),
	valor_produto FLOAT NOT NULL,
	PRIMARY KEY (id)
);

ALTER TABLE tb_vendas DROP COLUMN nome_produto;
ALTER TABLE tb_vendas DROP COLUMN valor_produto;

DESC tb_vendas;
DESC tb_produtos;

DROP TABLE tb_vendas;
DROP TABLE tb_produtos;

--------------------------------------------

 /* 3FN -> Terceira Forma Normal */

/*
 * Uma tabela está na 3FN se:
 *  - Estiver na 2FN
 *  - Não existirem dependências transitivas (um campo não chave depender de outro campo não chave
 */

CREATE TABLE tb_servicos(
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE tb_controle(
	id INT NOT NULL AUTO_INCREMENT,
	id_servico INT NOT NULL,
	qtd_horas INT NOT NULL,
	valor_hora FLOAT NOT NULL,
	total FLOAT NOT NULL,
	PRIMARY KEY (id, id_servico)
);

INSERT INTO tb_servicos (nome) VALUES
	('Pintura'), ('Marcenaria'), ('Limpeza');

SELECT * FROM tb_servicos ;

INSERT INTO tb_controle (id_servico, qtd_horas, valor_hora, total) VALUES
	(1, 3, 40, 120),
	(1, 2, 40, 80),
	(3, 8, 60, 480);

SELECT * FROM tb_controle;

/*
 * Problemas encontrados:
 * 	A coluna total depende das colunas qtd_horas e valor_hora, que não são colunas chave
 * 
 * Solução
 * 	Remover a coluna total e gerar esse valor no momento em que os registros forem consultados
 */

ALTER TABLE tb_controle DROP COLUMN total;
DESC tb_controle;

SELECT *, qtd_horas * valor_hora AS "Total" FROM tb_controle;

----------------------------------

 /* Nível de relacionamento entre tabelas (1:1, 1:N, N:N) */
 /*
  * 1:1 -> Relacionamento de 1 para 1. Considerando 2 tabelas (A e B) em uma relação de 1 pra 1, consideramos
  * que na tabela B há 1 e somente 1 linha correspondente a linha na tabela A
  * 
  * 1:N -> Relacionamento de 1 para muitos. Considerando 2 tabelas (A e B) em uma relação de 1 pra N, consideramos
  * que na tabela B há uma ou mais linhas correspondentes a uma linha na tabela A
  * 
  * N:N -> Relacionamento de Muitos para Muitos. Considerando 2 tabelas (A e B) em uma relação de N pra N, consideramos
  * que na tabela A há uma ou mais linhas correspondentes na tabela B, e vice-versa.
  * 
  * A:B -> 1:N
  * B:A -> 1:N
  */

/*
 * Vamos modelar um sistema de blog
 * 
 * Um blog deve ter usuários
 * Cada usuário pode possuir apenas 1 perfil
 * Cada usuário pode fazer 1 ou mais posts
 * Cada post pode ter 1 ou várias tags (#ti, #sql, #python)
 * 
 */

/* Relação de 1:1 entre users e profiles */

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(100) NOT NULL,
	password VARCHAR(100) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE profiles(
	id INT NOT NULL,
	nome VARCHAR(100) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES users(id)
);

DESC users;
DESC profiles;

INSERT INTO users (email, password) VALUES ('jose@email.com', '123456@');
INSERT INTO users (email, password) VALUES ('maria@email.com', '123456@');

INSERT INTO profiles (id, nome) VALUES (1, 'José da Silva');
INSERT INTO profiles (id, nome) VALUES (2, 'Maria da Dores');

SELECT * FROM users;
SELECT * FROM profiles;

INSERT INTO profiles (id, nome) VALUES (10, 'Maria das Dores');

# ---------------------------
/* Relação de 1:N entre users e posts */

CREATE TABLE posts(
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	title VARCHAR(200) NOT NULL,
	body TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO posts (user_id, title, body) VALUES 
	(1, 'Python', 'Python é legal'),
	(1, 'Javascript', 'Javascript é legal'),
	(2, 'C++', 'C++ é difícil');
	
SELECT * FROM posts;

/* Um usuário pode fazer 1 ou mais posts -> users 1 : N posts */
/* Um post pertence a apenas 1 usuário -> posts 1 : 1 users */

/*
 * O comando abaixo não funcionará, pois não existe um registro na tabela users onde o user_id seja 10000, dessa maneira conseguimos garantir
 * a integridade dos dados nessa relação.
 */
INSERT INTO posts (user_id, title, body) VALUES (10000, 'Programar', 'Programar é legal');


/* Relação N:N entre posts e tags */
/* posts 1 : N tags */
/* tags 1 : N posts */
/* tags N : N */

/* Quando temos uma relação de N:N, precisamos criar uma tabela associativa, ou seja, uma tabela que fará
 * a associação dos ids das 2 tabelas da relação
 */

CREATE TABLE tags(
	id INT NOT NULL AUTO_INCREMENT,
	tag VARCHAR(200) NOT NULL,
	PRIMARY KEY (id)
);

DESCRIBE tags;

INSERT INTO tags(tag) VALUES
	('python'),
	('programação'),
	('ti'),
	('curso');
	
SELECT * FROM tags;

/* Agora criamos a tabela associativa posts_tags */
CREATE TABLE posts_tags(
	post_id INT NOT NULL,
	tag_id INT NOT NULL,
	PRIMARY KEY (post_id, tag_id),
	FOREIGN KEY (post_id) REFERENCES posts(id),
	FOREIGN KEY (tag_id) REFERENCES tags(id)
);

DESCRIBE posts_tags;

/* Vamos associar AS tags #python e #programação ao post de id 1 */
INSERT INTO posts_tags(post_id, tag_id) VALUES (1, 1);
INSERT INTO posts_tags(post_id, tag_id) VALUES (1, 2);

/* Tentando inserir um valor de post_id que não existe na tabela posts */
INSERT INTO posts_tags(post_id, tag_id) VALUES (1000000, 1);

SELECT * FROM posts_tags ;

/* ------------------------------------ */

/* Sistema de cursos */
/*
 * Precisamos ter um registro de alunos
 * Precisamos ter um registro de instrutores
 * Precisamos ter um registro de cursos
 * 
 * Precisamos ter o controle de quais instrutores estão dando determinados cursos
 * Precisamos ter o controle de quais alunos estão em determinados cursos
 * 
 * Deve haver uma separação entre dados de usuário e perfil de usuário
 * Um instrutor pode dar nenhum, 1 ou mais cursos
 * Um instrutor pode ser substituído em uma turma
 * Um aluno pode fazer nenhum, 1 ou mais cursos
 */

-- Nesse exemplo, vamos separar em tabelas o que são dados de acesso ao sistema e o que são dados de perfil do aluno
-- tabela usuarios -> dados de acesso
-- tabela perfis -> dados pessoais do aluno

CREATE TABLE usuarios (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(200) NOT NULL,
	senha VARCHAR(200) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE perfis (
	id INT NOT NULL,
	nome VARCHAR(200) NOT NULL,
	data_nascimento DATE NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES usuarios(id)
);

/*
 
	usuarios
	--------
	id		email		senha
	1		1@email		1234
	2		2@email		1234
	3		3@email		1234

	perfis
	------
	id		nome
	1		José
*/

/* Criando a tabela instrutores */
CREATE TABLE instrutores(
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	PRIMARY KEY (id)
);

/* Criando a tabela de cursos */
CREATE TABLE cursos(
	id INT NOT NULL AUTO_INCREMENT,
	nome VARCHAR(200) NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO usuarios (email, senha) VALUES 
('jose@email.com', '123456'),
('maria@email.com', '123456'), 
('joao@email.com', '123456'), 
('amanda@email.com', '123456'), 
('lorena@email.com', '123456');

INSERT INTO perfis (id, nome, data_nascimento) VALUES
	(1, 'José', '1990-12-03'),
	(2, 'Maria', '1988-11-23'),
	(3, 'João', '1993-04-29'),
	(4, 'Amanda', '1992-01-12'),
	(5, 'Lorena', '1991-07-10');
	

INSERT INTO instrutores (nome) VALUES 
	('Bruno'), ('Ricardo'), ('Manuel'), ('Carla'), ('Thays');
	
INSERT INTO cursos (nome) VALUES
	('Introdução a Programação'),
	('Preparatório Certificado Azure'),
	('Orientação a Objetos em Java'),
	('Formação DevOps'),
	('Introdução a Machine Learning');
	
CREATE TABLE turmas(
	id INT NOT NULL AUTO_INCREMENT,
	curso_id INT NOT NULL,
	data_inicio DATE NOT NULL,
	data_fim DATE NULL,
	observacoes VARCHAR(200) NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

/*
 * cursos
 * ------
 * id		nome
 * 1		Programação em Python
 * 2		Programação em Java
 * 3		Programação em C#
 * 
 * turmas
 * ------
 * id		id_curso		observacoes
 * 1		1				
 * 2		3				
 * 3		1
 * 
 * 
 */

INSERT INTO turmas(curso_id, data_inicio, data_fim, observacoes) VALUES
	(1, '2021-01-13', '2021-04-13', NULL),
	(2, '2021-02-20', '2021-03-20', NULL),
	(2, '2021-03-01', '2021-05-01', NULL),
	(4, '2021-02-01', '2021-04-01', NULL),
	(1, '2021-01-30', '2021-04-30', 'Turma do programa social');
	
SELECT * FROM turmas;

/*
 * Um instrutor ele pode dar aula em 1 ou mais turmas
 * Uma turma pode ter 1 ou mais instrutores
 * instrutores 1 : N turmas
 * turmas 1 : N instrutores
 * turmas N : N instrutores
 */

CREATE TABLE instrutores_turmas (
	instrutor_id INT NOT NULL,
	turma_id INT NOT NULL,
	PRIMARY KEY (instrutor_id, turma_id),			-- Chave primária composta
	FOREIGN KEY (instrutor_id) REFERENCES instrutores(id),
	FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

/*
 * Um aluno pode estar matriculado em 1 ou mais turmas
 * Uma turma pode ter 1 ou mais alunos
 * alunos 1 : N turmas
 * turmas 1 : N alunos
 * turmas N : N alunos
 */

CREATE TABLE alunos_turmas(
	aluno_id INT NOT NULL,
	turma_id INT NOT NULL,
	PRIMARY KEY (aluno_id, turma_id),
	FOREIGN KEY (aluno_id) REFERENCES usuarios(id),
	FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

INSERT INTO instrutores_turmas (instrutor_id, turma_id) VALUES
	(5, 1),
	(3, 2);
	
SELECT * FROM instrutores_turmas ;

INSERT INTO alunos_turmas (aluno_id, turma_id) VALUES 
	(1, 1),
	(2, 1),
	(4, 1);
	
INSERT INTO alunos_turmas(aluno_id, turma_id) VALUES 
	(3, 2),
	(5, 2);
	
SELECT * FROM alunos_turmas at2 ;

-- Joins
-- As consultas com Joins permitem que retornemos dados de várias tabelas na mesma consulta.

/*
 * INNER JOIN	
 * LEFT JOIN
 * RIGHT JOIN
 */

/* Selecionar todos os cursos que possuem turmas */
SELECT c.nome, t.data_inicio, t.data_fim FROM cursos c INNER JOIN turmas t ON c.id = t.curso_id ;

/* Selecionar os cursos que não possuem turmas */
SELECT c.nome, t.data_inicio, t.data_fim
FROM cursos c 
LEFT JOIN turmas t ON c.id = t.curso_id WHERE t.curso_id IS NULL;

/* Quais instrutores estão dando quais cursos */
SELECT i.id, i.nome, c.nome, t.data_inicio, t.data_fim FROM instrutores i
INNER JOIN instrutores_turmas it ON i.id = it.instrutor_id
INNER JOIN turmas t ON it.turma_id = t.id
INNER JOIN cursos c ON t.curso_id = c.id;

-- Inserindo alunos que não estão em turmas
INSERT INTO usuarios (email, senha) VALUES
	('daiane@email.com', '12345'),
	('eduarda@email.com', '12345'),
	('giselle@email.com', '12345');
	
INSERT INTO perfis (id, nome, data_nascimento) VALUES
	(6, 'Daiane', '1991-05-03'),
	(7, 'Eduarda', '1992-10-11'),
	(8, 'Giselle', '1995-04-09');