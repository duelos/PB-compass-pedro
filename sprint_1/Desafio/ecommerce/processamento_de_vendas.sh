#!/bin/bash

DATA=$(date +%Y%m%d)

mkdir /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas

cp /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/dados_de_vendas.csv /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/

mkdir /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup

cp /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/dados_de_vendas.csv /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/dados-$DATA.csv

mv /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/dados-$DATA.csv /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/backup-dados-$DATA.csv
touch /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATA.txt

#RELATORIO

DATAARQ=$(date +%Y%m%d) #DATA DO ARQUIVO
DATA=$(date "+%Y/%m/%d %H:%M") #DATA DO SISTEMA
PRIMEIRORE=$(cat /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/backup-dados-$DATAARQ.csv|head -2|tail -1) #PRIMEIRO REGISTRO DE VENDA
ULTIMORE=$(cat /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/backup-dados-$DATAARQ.csv|tail -1) #ULTIMO REGISTRO DE VENDA
QNTITENS=$(cat /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/backup-dados-$DATAARQ.csv|cut -d "," -f2|sed 1d|sort|uniq|wc -l) #QUANTIDADE DE PRODUTOS DIFERENTES
DEZPRIMEIRAS=$(cat /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/backup-dados-$DATAARQ.csv|head -10)

echo "=====RELATORIO DE VENDAS=====" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo " " >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "DATA DO SISTEMA: $DATA" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "=============================" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "PRIMEIRO REGISTRO DE VENDA:" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "$PRIMEIRORE" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo " " >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "ULTIMO REGISTRO DO SISTEMA:" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "$ULTIMORE" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo " " >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "QUANTIDADE TOTAL DE ITENS DIFERENTES VENDIDOS:$QNTITENS " >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo " " >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "10 PRIMEIRAS LINHAS:" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "$DEZPRIMEIRAS" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo " " >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
echo "============================" >> /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/relatorio-$DATAARQ.txt
zip /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/backup-dados-$DATAARQ.zip /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/backup-dados-$DATAARQ.csv
rm /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/backup/backup-dados-$DATAARQ.csv
rm /home/pedro/pb-pedro-henrique/sprint_1/Desafio/ecommerce/vendas/dados_de_vendas.csv



