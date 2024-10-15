-- Resolucao Questao 5

select distinct autor.nome
from livro left join autor on livro.autor = autor.codautor
left join editora on livro.editora = editora.codeditora
left join endereco on editora.endereco = endereco.codendereco
where endereco.estado != 'RIO GRANDE DO SUL' and endereco.estado != 'PARANÁ'
order by autor.nome
