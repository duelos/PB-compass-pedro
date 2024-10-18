-- Resolucao Questao 13

select cdpro,tbvendas.nmcanalvendas, tbvendas.nmpro, sum(tbvendas.qtd) as quantidade_vendas
from tbvendas
where status = 'Concluído'
group by cdpro, tbvendas.nmcanalvendas, tbvendas.nmpro
order by quantidade_vendas
limit 10
