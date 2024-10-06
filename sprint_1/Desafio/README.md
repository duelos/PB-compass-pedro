# Desafio

O desafio consiste em criar 2 scripts, um deles irá criar uma árvore de diretórios e arquivos, coletar dados de uma planilha de vendas e gerar relatórios, o outro, irá consolidar todos os relatórios gerados.

# ETAPAS

## Primeiro script:

[Etapa_1](../Evidências/etapa_1.png)

### Nessa primeira etapa:
* Eu estou criando o diretório "vendas" com o comando mkdir(make directory).

* Após isso, eu copio com o comando cp(copy) o arquivo que baixei "dados_de_vendas.csv" para esse diretório.

* Crio outro diretório chamado "backup".

* Utilizo o comando cp em "dados_de_vendas.csv" novamente, porém desta vez copiando para o diretório "backup" e estou renomeando-o para "dados-e a data do sistema", para isso, eu criei a variável "DATA" que armazena o comando para exibir a data.

* Utilizo o comando mv para renomear o arquivo "dados-DATA" para "backup-dados-DATA".

* Utilizo o comando touch para criar um arquivo txt chamado "relatorio-DATA" no diretório backup.

[Etapa_2](../Evidências/etapa_2.png)

### Nessa segunda etapa:

A segunda etapa é referente ao relatório.

#### VARIAVEIS
* Criei várias variáveis para deixar o código mais flúido e compreensivel. As duas primeiras armazenam a data, a primeira delas "DATAARQ" será utilizada para saber a data do arquivo, pois como visto anteriormente, salvei os arquivos com a data em seu nome. A segunda, "DATA", Servirá apenas para mostrar a data do sistema, bem como as horas e minutos.

* A variável "PRIMEIRORE" armazena o primeiro registro de venda do arquivo, utiliza o comando cat para abrir o arquivo no diretório backup, "backup-dados-data", com a saída desse comando, ele realiza o comando cut para fatiar e exibir apenas o que eu colocar como requisito, utilizando ' -d "," ' estou dizendo que os delimitadores/separadores do arquivo é uma vírgula, e em -f5 digo que estou procurando por espaços no arquivo, sendo assim, ele irá procurar no 5º espaço separado por vírgula, que na planilha, é o espaço da data da operação, e com a saída disso, o comando head -n2 serve para ele mostrar apenas as 2 primeiras linhas, e tendo em vista que a primeira é o cabeçalho, o tail -1 me mostrará a ultima linha, que é referente a primeira linha de produto da planilha.

* A variável "ULTIMORE" armazena o último registro de venda do arquivo, em questão de comandos, é igual o "PRIMEIRORE", apenas com a falta do comando head, já que queremos o último registro, ficamos apenas com o tail -1.

* A variável "QNTITENS" irá me mostrar a quantidade total de itens diferentes vendidos, utilizamos o comando cat com o mesmo fim, porém agora no comando cut, usamos o -f2, para procurar no espaço de "produtos" da planilha, com a saída dessa informação, uso o sed 1d para deletar a primeira linha do arquivo, que é o cabeçalho, o comando sort ordena a lista. O comando uniq elimina repetições de palavras ou números iguais, porém, tem a restrição de fazer isso somente se a repetição for sequencial, justificando a utilização do sort, o comando wc -l irá contar a quantidade de linhas. Em resumo, o comando irá buscar no espaço "produtos" da planilha, e irá contar a quantidade de linhas de produtos diferentes.

* A variável "DEZPRIMEIRAS" faz o cat no arquivo e utiliza head -10, buscando as 10 primeiras linhas do arquivo.

#### ECHOS

* Essa parte é bem simples, estou utilizando o comando echo para mostrar uma linha de texto e exibir as váriaveis, todos os echos estão com as saídas apontadas para o arquivo "relatorio-DATAARQ", esta parte é mais organização.

###
[Etapa_3](../Evidências/etapa_2.png)

### Nessa terceira etapa:

* Utilizei o comando zip para compactar o arquivo csv, salvando todos os diretórios até o arquivo.

* removi o arquivo csv do diretório backup.

* removi o arquivo csv do diretõrio vendas.

## Agendamento no crontab:

[Agenda](../Evidências/crontab.png)

* O agendamento do crontab exige 5 asteriscos, o primeiro é referente aos minutos, o segundo às horas, o terceiro é o dia do mês, o quarto ao mês e o quinto ao dia da semana. Após isso você coloca o caminho do seu script para ele ser executado.

## Segundo script:

[Segundo_script](../Evidências/consolidador.png)

* Utilizo o comando touch para criar o arquivo "relatorio_final.txt"

* O echo para mostrar no arquivo

* Uso o cat para abrir todos os arquivos do diretório backup que terminam em .txt e aponto saída disso para o arquivo que criamos.

[relatorio_final](../Evidências/relatorio_final_1.png)

[relatorio_final](../Evidências/relatorio_final_2.png)

Tendo isso como resultado.






