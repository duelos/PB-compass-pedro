-- Resolucao Questao 7

select nome
from autor left join livro on autor.codautor = livro.autor
where publicacao is null
group by nome
