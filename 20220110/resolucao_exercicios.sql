/* Resolução Exercícios Aula 01 */

# a)
CREATE DATABASE	exercicios_aula01;
USE	exercicios_aula01;

# b)
CREATE TABLE uzuarios(
	nome varchar(100),
	sobrenome varchar(50),
	idade int,
	imail varchar(50)
);

# c)
ALTER TABLE uzuarios RENAME TO usuarios;

# d)
ALTER TABLE	usuarios CHANGE imail email varchar(50);

# e)
ALTER TABLE usuarios ADD cidade varchar(30);

# f)
ALTER TABLE usuarios DROP COLUMN sobrenome;

# g)
INSERT INTO usuarios(nome, idade, email, cidade) VALUES 
	('Jéssica', 20, 'jessy.gomes@gmail.com', 'Blumenau'),
	('Cleiton', 32, 'cleiton.crispin@gmail.com', 'Brusque'),
	('Carolina', 13, 'carol.ventura@hotmail.com', 'Blumenau'),
	('Victor', 17, 'victor.almeida@gmail.com', 'Gaspar'),
	('Joana', 42, 'joana.prudente@live.com', 'Blumenau');
	
# h)
SELECT * FROM usuarios;

# i)
SELECT * FROM usuarios WHERE idade > 17;

# j)
SELECT * FROM usuarios u WHERE cidade = 'Blumenau' AND idade < 18;

# k)
UPDATE usuarios SET idade = 36 WHERE nome = 'Joana';

# l)
DROP DATABASE exercicios_aula01;