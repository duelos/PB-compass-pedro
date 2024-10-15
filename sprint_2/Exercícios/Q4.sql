-- Resolucao Questao 4

select nome, codautor,nascimento,count(livro.cod) as quantidade
from autor left join livro on autor.codautor = livro.autor
group by  nome, codautor, nascimento
order by nome
