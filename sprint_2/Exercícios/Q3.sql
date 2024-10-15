-- Resolucao Questao 3

select count(livro.cod) as quantidade, editora.nome, endereco.estado, endereco.cidade
from endereco inner join editora on endereco.codendereco = editora.endereco
inner join livro on editora.codeditora = livro.editora

group by editora.nome, endereco.estado, endereco.cidade
order by quantidade desc
limit 5
