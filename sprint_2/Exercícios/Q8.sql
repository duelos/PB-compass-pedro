-- Resolucao Questao 8

with tabela_vendas as (
select vdd.cdvdd, vdd.nmvdd, count(cdven) as contagem
from tbvendedor as vdd left join tbvendas as ven on vdd.cdvdd = ven.cdvdd
where status = 'Concluído'
group by vdd.cdvdd, vdd.nmvdd
)

select cdvdd, nmvdd
from tabela_vendas
order by contagem desc
limit 1
