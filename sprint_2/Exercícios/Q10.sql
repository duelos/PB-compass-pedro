-- Resolucao Questao 10

with tabela as (
select vdd.cdvdd as codigo, nmvdd as vendedor, sum(qtd * vrunt) as valor_total_vendas, perccomissao
from tbvendedor as vdd left join tbvendas as ven on vdd.cdvdd = ven.cdvdd
where status = 'Concluído'
group by vdd.cdvdd,vdd.nmvdd, vdd.perccomissao
)

select vendedor, valor_total_vendas, round((valor_total_vendas * perccomissao) / 100 , 2) as comissao
from tabela
order by comissao desc
