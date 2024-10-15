-- Resolucao Questao 6

select codautor, nome, count(livro.publicacao) as quantidade_publicacoes
from livro left join autor on livro.autor = autor.codautor
group by codautor, nome
order by quantidade_publicacoes desc
limit 1

