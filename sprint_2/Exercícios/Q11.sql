-- Resolucao Questao 11

select  cdcli, nmcli, sum(qtd * vrunt) as gasto
from tbvendas
group by cdcli, nmcli
order by gasto desc
limit 1
