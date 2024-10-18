-- Querry do CSV cincoeditoras

with tabela as (
select count(livro.cod) as quantidade, editora.nome, endereco.estado,editora.codeditora, endereco.cidade
from endereco inner join editora on endereco.codendereco = editora.endereco
inner join livro on editora.codeditora = livro.editora

group by editora.nome, endereco.estado, endereco.cidade
order by quantidade desc
limit 5
)
select  codeditora as CodEditora, nome as NomeEditora, quantidade as QuantidadeLivros
from tabela
