
# Programação Orientada a Objetos Em Python

 * POO (OOP) um paradigma de programaão fortemente baseada no conceito de objetos, que podem conter dados (atributos ou propriedades) e código
   (na forma de métodos).

 * Um paradigma de programação é a maneira como classificamos um programa de acordo com a sua organização.
 * Alguns dos paradigmas de programação
   * Programação imperativa
     * Procedural
       * Baseado em procedures (funções)
     * Orientado a Objetos
       * Paradigma onde o conceito central é o objeto, sendo o objeto uma representação de uma entidade do mundo real.
   * Programação declarativa
     * Funcional
       * Todas as coisas no nosso programa são funções
       
 * Terminologia
   * Objeto
     * É a instância de uma classe, ou uma entidade criada a partir de uma classe
   * Classe
     * É o modelo a partir do qual instanciamos os objetos. Aqui definimos as características da classe e o comportamento
       * dos objetos instanciados a partir dessa classe.
   * Atributos
     * São características da entidade representada por uma determinada classe
   * Métodos
     * São as ações que um objeto pode realizar. Além disso, os métodos server pra alterar o estado do próprio objeto.
 

# Exercício

## Sistema de Folha de Pagamento

No nosso sistema de folha de pagamento, existem 3 tipos de funcionários:
* Funcionário CLT: Recebe um valor fixo de salário.
* Funcionário Terceirizado: Tem seu salário definido como a quantidade de horas trabalhadas x o valor da hora.
* Funcionário Comissionado: Tem seu salário definido como uma porcentagem do valor total de vendas que ele realizou.

O Sistema de folha de pagamento deve calcular o salário de cada funcionário seguindo as regras acima descritas.

Todo funcionário possui um nome e um código identificador (id).

* Criar um método chamado salvar_folha na classe FolhaDePagamento
* Esse método vai salvar a folha de pagamento calculada em um novo arquivo csv chamado salarios.csv
* Esse arquivo terá a seguinte estrutura:
````csv
id;nome;salario
7058a2d0-3ba6-4bff-af6a-f64e63a253cb;Helena;2349.13
````
* Deve-se criar um método na classe ArquivoCSV chamado salvar
* Esse método vai receber a lista de registros que devem ser salvos (incluindo o cabeçalho do arquivo)
* O id é gerado usando a função str(uuid4()) do pacote uuid (`from uuid import uuid4()`)