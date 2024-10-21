# Desafio

O desafio consiste em aplicar regras de normalização em um banco de dados que foi disponibilizado e após isso, aplicar o modelo relacional e com base nele, fazer um modelo dimensional.

# Etapas

## Criando Tabelas
* O começo da normalização vem com a separação de tabelas pelas entidades e os valores que lhe dizem respeito, então criei cada tabela e coloquei dentro delas as colunas que as atribuem. Para cada tabela eu coloquei uma chave primaria com o ID no nome e os tornei únicos para evitar que se repitam registros pois a NF1 diz sobre a atomicidade e unicidade dos dados, ou seja, cada célula da tabela deve armazenar um único valor, não conjuntos de valores, listas ou múltiplos valores. Já o NF2 que diz que todos os atributos não-chave devem depender da chave primária, porém como não temos atributos compostos, não há evidência de aplicacão. A NF3 diz que um atributo não-chave não pode depender de outro atributo não-chave, mas não há esse tipo de relação no nosso banco de dados.
* Colocando sempre o tipo de coluna, utilizei NOT NULL para caso for implementado alguma linha na tabela, que não permita valores nulos
* Para cada tabela eu coloquei uma chave primaria com o ID no nome e os tornei únicos para evitar que se repitam registros
* No que diz respeito aos relacionamentos, eu relacionei Carro com Combustivel, para que fique registrado qual o combustível que cada carro usa, e a tabela Locacoes possui relacionamento com todas as outras, fiz a ligação delas referenciando as chaves estrangeiras com essa tabela utilizando o comando 'FOREIGN KEY'.
[Etapa_1](../Evidências/Etapa_1.png)


## Inserindo dados em cada tabela
Inseri os dados das tabelas dentro de cada tabela com o 'insert into'.
[Etapa_2](../Evidências/Etapa_2.png)

## Criando views para montar o modelo dimensional
Como foi aconselhado, fiz o uso de 'create view' para criar visualizações e facilitar o processo de fazer o modelo dimensional. Onde no nosso caso, a tabela fato seria a tabela "Locacoes" e as dimensões são as tabelas "Cliente", "Vendedor", "Veiculo" e "Combustivel"
[Etapa_3](../Evidências/Etapa_3.png)

# Resultados

*Tabelas e Views*
[Tabelas_e_Views](../Evidências/Tabelas.png)

*Modelo Relacional*
[Modelo_Relacional](./Modelo%20Relacional%20x%20Dimensional/Modelo%20Relacional.png)

*Modelo Dimensional*
[Modelo_Dimensional](./Modelo%20Relacional%20x%20Dimensional/Modelo%20Dimensional.png)

