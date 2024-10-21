# Desafio

O desafio consiste em aplicar regras de normalização em um banco de dados que foi disponibilizado e após isso, aplicar o modelo relacional e com base nele, fazer um modelo dimensional.

# Etapas

## Criando Tabelas
* O começo da normalização vem com a separação de tabelas pelas entidades e os valores que lhe dizem respeito, então criei cada tabela e coloquei dentro delas as colunas que os atribuem.
* Colocando sempre o tipo de coluna, utilizei NOT NULL para caso for implementado alguma linha na tabela, que não permita valores nulos
* Para cada tabela eu coloquei uma chave primaria com o ID no nome
* No que diz respeito aos relacionamentos, eu relacionei Carro com Combustivel, para que fique registrado qual o combustível que cada carro usa, e a tabela Locacoes possui relacionamento com todas as outras, fiz a ligação delas referenciando as chaves estrangeiras com essa tabela utilizando o comando 'FOREIGN KEY'.
[Etapa_1](../Evidências/Etapa_1.png)


## Inserindo dados em cada tabela
Inseri os dados das tabelas dentro de cada tabela com o 'insert into'.
[Etapa_2](../Evidências/Etapa_2.png)

## Criando views para montar o modelo dimensional
Como foi aconselhado, fiz o uso de 'create view' para criar visualizações e facilitar o processo de fazer o modelo dimensional.
[Etapa_3](../Evidências/Etapa_3.png)

## Resultados

*Tabelas e Views*
[Tabelas_e_Views](../Evidências/Tabelas.png)

*Modelo Relacional*
[Modelo_Relacional](./Modelo%20Relacional%20x%20Dimensional/Modelo%20Relacional.png)

*Modelo Dimensional*
[Modelo_Dimensional](./Modelo%20Relacional%20x%20Dimensional/Modelo%20Dimensional.png)

