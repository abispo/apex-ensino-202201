# Mostra todas as bases de dados do servidor
SHOW DATABASES;

# Define o banco de dados onde os comandos serão executados;
USE aula_20220112;


# Retorna todos os registros da tabela customers
SELECT * FROM customers c;

/***
 * OPERADORES RELACIONAIS
 * = IGUAL A
 * > MAIOR QUE
 * < MENOR QUE
 * >= MAIOR OU IGUAL A
 * <= MENOR OU IGUAL A
 * <> DIFERENTE
**/

# Filtrando todos os clientes que possuem crédito abaixo de 50000
SELECT * FROM customers WHERE creditLimit < 50000;

# Ordenando os clientes do limite de crédito maior para o menor
# ORDER BY <nome_da_coluna> [ASC] - Ordena os itens da coluna de forma ascendente (padrão)
# ORDER BY <nome_da_coluna> DESC - Ordena os itens da coluna de forma decrescente.
SELECT * FROM customers WHERE creditLimit < 100000 ORDER BY creditLimit DESC;

# Ordenar os clientes pelo customerNumber. Queremos trazer os clientes que possuem código entre
# 200 e 300
SELECT * FROM customers c WHERE customerNumber >= 200 AND customerNumber <= 300;

# Retornar todos os customers onde a coluna country não seja USA;
SELECT * FROM customers c WHERE country <> "USA";

/***
 * OPERADORES LÓGICOS
 * AND 			E
 * OR			OU
 * IN			ESTÁ EM (Está contido em algo)
 * NOT IN		NÃO ESTÁ EM (Não está contido em algo)
 * LIKE			É/É PARECIDO ()
 * NOT LIKE		NÃO É/NÃO É PARECIDO
 * BETWEEN		ENTRE (Está entre valores)
***/

SELECT * FROM products p ;

# Usamos o IN/NOT IN pra testar se um determinado valor está dentro de uma coleção

# Vamos verificar se a linha de produtos 'SpaceShips' está na tabela
SELECT * FROM products p WHERE productLine IN ('SpaceShips');

# Vamos verificar se as linhas de produtos 'Planes' e 'Ships' estão na tabela
SELECT * FROM products p WHERE productLine IN ('Planes', 'Ships');

# Vamos trazer todas as linhas de produtos que não sejam 'Trains'
SELECT * FROM products p WHERE productLine NOT IN ('Trains');

/* LIKE / NOT LIKE */

# Filtrando todos os clientes onde o nome comece com 'Mini'
# Usamos o wildcard '%' pra filtrar as letras das strings
SELECT * FROM customers c WHERE customerName LIKE 'Mini%';

SELECT * FROM customers c WHERE customerName LIKE '%Collectables';

SELECT * FROM customers c WHERE customerName LIKE '%Auto%';

SELECT * FROM customers c WHERE customerName LIKE '%ne%to%'

# BETWEEN filtra os dados entre 2 valores
SELECT * FROM customers c WHERE creditLimit BETWEEN 50000 AND 100000;

/* OPERADORES ARITMÉTICOS */
/***
	+ 		ADIÇÃO
	-		SUBTRAÇÃO
	* 		MULTIPLICAÇÃO
	/		DIVISÃO
	%		RESTO DA DIVISÃO
***/


SELECT 10 * 20;

SELECT 5 % 4;

SELECT 6 % 2;

# Retornar productCode, productName, productLine, quantityInStock, buyPrice, e a
# multiplicação entre as 2 últimas colunas
# Podemos modificar o nome exibido da coluna usando a palavra 'AS'
SELECT 
	productCode,
	productName,
	productLine, 
	quantityInStock,
	buyPrice,
	quantityInStock * buyPrice AS 'Preço Total'
FROM products p ;

/* ALGUMAS FUNÇÕES DA LINGUAGEM */

# COUNT() -> Conta a quantidade de registros
SELECT count(*) FROM orders o ;

# MAX() / MIN() -> Retornam o valor máximo e mínimo de uma coluna, respectivamente.
SELECT max(quantityInStock) FROM products p ;
SELECT min(quantityInStock) FROM products p ;

# AVG() -> Retorna a média de valores de uma coluna
SELECT avg(quantityInStock) FROM products p ;

# SUM() -> Soma todos os valores de uma coluna
SELECT sum(quantityInStock) FROM products p ;

# DISTINCT -> Retorna apenas valores não repetidos
SELECT DISTINCT status FROM orders;