-- Resolucao Questao 12

select cddep, nmdep, dtnasc, sum(qtd * vrunt) as valor_total_vendas
from tbvendedor as vdd left join tbvendas as ven
on vdd.cdvdd = ven.cdvdd
left join tbdependente as dep
on vdd.cdvdd = dep.cdvdd
where status = 'Concluído'
group by cddep, nmdep, dtnasc
order by valor_total_vendas
limit 1
