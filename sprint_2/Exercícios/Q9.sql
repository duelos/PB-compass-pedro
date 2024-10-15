-- Resolucao Questao 9

with tabela as (
select cdpro, nmpro , count(*) as contagem
from tbvendas
where dtven between '2014-02-03 00:00:00' and '2018-02-02 00:00:00'
and status = 'Concluído'
group by cdpro, nmpro
    )
select cdpro, nmpro
from tabela
order by contagem desc
limit 1










