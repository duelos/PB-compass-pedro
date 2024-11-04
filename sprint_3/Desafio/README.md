# Desafio 
Nessa sprint, o desafio gira em torno de utiliar as bibliotecas 'pandas' e 'matplotlib' para extração e geração de gráficos a partir do csv 'googleplaystore.csv' que nos foi disponibilizado.


# Etapa 1 - Preparando o ambiente
# Importando bibliotecas, lendo o csv e removendo duplicações
[etapa_1](../Evidências/etapa1.png)


# ETAPA 2 - Grafico do TOP 5
## Faça um gráfico de barras contendo os top 5 apps por número de instalação

* Primeiro faço a remoção dos caracteres indesejados na coluna 'Installs' com o .replace, faço uso do .loc pois facilita bastante acessar todas as linhas na coluna 'Installs' do DataFrame df_sem_duplicatas, _regex_ para fazer o uso das expressões regulares, e troco o _Free_ por _0_
* Conversão da Coluna 'Installs' para Valores Numéricos com *'pd.to_numeric'* e qualquer valor que não puder ser convertido é transformado em NaN, usando o parâmetro *errors='coerce'*
* Remoção de Linhas com Valores NaN em 'Installs' com o *'dropna'*
* Com o *'astype(int)'* converte os valores da coluna 'Installs' para int, garantindo que a coluna é do tipo inteiro, o que é necessário para funções como *nlargest*. 
* O plt.figure(figsize=(12, 8)) - *Cria figura com tamanho 12,8*
plt.bar(top5['App'], top5['Installs'], color='skyblue') - *Cria um grafico '.bar' de barra com o eixo X sendo o 'App' e o Y sendo 'Installs' e as barras são coloridas de azul claro*
plt.xlabel("Aplicativos") - *determina o nome do eixo X*
plt.ylabel("Número de Instalações") - *determina o nome do eixo Y*
plt.title("Top 5 aplicativos") - *determina o titulo*
plt.xticks(rotation=45) - *determina a rotacao de 45 graus*
plt.show() - *mostra o grafico*

[etapa_2](../Evidências/etapa2.png)

### Tive isso como resultado:
[grafico](../Evidências/grafico_etapa_2.png)

# ETAPA 3 - Grafico de Pizza
## Faça um gráfico de pizza mostrando as categorias de apps existentes no dataset de acordo com a frequência em que elas aparecem

* Faço a contagem de ocorrências das categorias com o *'value_counts'*
* utilizo o *'pie'* para criar o grafico de pizza
* *'autopct'* para determinar a quantidade de decimais que as porcentagens terão, e o *'starangle'* para ditar o ângulo de inicio do gráfico 
* *'.axis('equal')'* permite que o gráfico fique mais proporcional

[etapa_3](../Evidências/etapa3.png)

### Tive isso como resultado:
[grafico](../Evidências/grafico_etapa_3.png)

# ETAPA 4 - Item mais caro
## Mostre qual o app mais caro existente no dataset

* Uso o idxmax para procurar o indice maximo da coluna Price

[etapa_4](../Evidências/etapa4.png)

# ETAPA 5 - Quantos Apps qualificados "mature +17"
## Mostre quantos apps são classificados como 'Mature 17+'

* Crio um filtro que seleciona somente as linhas onde a coluna 'Content Rating' tem o valor 'Mature 17+'
* *.shape* é um atributo que retorna uma tupla com o número de linhas e colunas do data frame, o '[0]' pega o primeiro elemento da tupla, que nos dá a contagem de aplicativos que atendem o criterio.

[etapa_5](../Evidências/etapa5.png)

# ETAPA 6 - Top 10 apps Review
## Mostre os top 10 apps por número de reviews bem como o respectivo número de reviews. Ordene de forma decrescente por número de reviews.

### Selecionar os 10 aplicativos com o maior número de avaliações, sem duplicatas de nome

* f_sem_duplicatas['Reviews'] = pd.to_numeric(df_sem_duplicatas['Reviews'].str.replace(r'[\D]','', regex=True), errors='coerce') - Retiro caracteres indesejados

* df_unique_apps = df_sem_duplicatas.sort_values(by='Reviews', ascending=False).drop_duplicates(subset='App') - uso o *'sort_values'* para ordenar a coluna e o *ascending=False* para determinar que é decrescente, e *drop_duplicates* para retirar os duplicados da coluna 'App'

[etapa_6](../Evidências/etapa6.png)

# ETAPA 7 - Calculos
## Top 10 apps por rating
* top10appsrating = df_sem_duplicatas.nlargest(10, 'Rating') - armazeno na variável o valor dos 10 resultados mais altos da tabela Rating
* resultadotop10 = top10appsrating[['App','Rating']] - Exibo somente as tabelas App e Rating

[etapa_7](../Evidências/etapa7_1.png)

## App com mais reviews
* appmaisreviews = df_sem_duplicatas.nlargest(1,'Reviews') - pego o maior valor de Reviews
* resultado_app_reviews = appmaisreviews[['App','Reviews']] - exibo somente as tabelas App e Reviews

[etapa_7](../Evidências/etapa7_2.png)

# Etapa 8 - Gráfico de linha e dispersão
* Devemos criar 2 gráficos de algum indicador do dataset, farei com o rating medio das categorias e um de relacionar a coluna de instalações com a de rating.
## Gráfico de linha
* rating_por_categoria = df_sem_duplicatas.groupby('Category')['Rating'].mean() - utilizo *mean*para tirar a média de rating em categorias

* plt.plot(rating_por_categoria.index, rating_por_categoria.values, color= 'blue', marker='o') - indico que o gráfico será do tipo linha
* plt.xticks(rotation=90) - indico rotação de 90 graus
* plt.grid(True) - adiciono grades para ficar mais facil de compreender o gráfico
* plt.tight_layout() - refino o layout do gráfico

[etapa_8](../Evidências/etapa8_1.png)

## Gráfico de dispersão
* plt.scatter(df_sem_duplicatas['Installs'], df_sem_duplicatas['Rating'], color = 'green') - *.scatter* indico que o grafico será do tipo dispersão
* plt.xscale('log') - defino a escala como logarítmica pois os valores eram muito altos e assim o gráfico fica mais fácil de visualizar 

[etapa_8](../Evidências/etapa8_2.png)