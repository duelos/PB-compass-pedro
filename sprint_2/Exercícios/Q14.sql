-- Resolucao Questao 14

select estado, round(avg(qtd * vrunt),2)gastomedio
from tbvendas
where status = 'Concluído'
group by estado
order by gastomedio desc
