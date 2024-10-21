-- Resolucao DezLivros

select cod as CodLivro,livro.titulo as Titulo,autor as CodAutor,a.nome as NomeAutor, livro.valor as Valor, editora as CodEditora, e.nome as NomeEditora
from livro left join main.autor a on livro.autor = a.codautor
left join main.editora e on livro.editora = e.codeditora
order by  valor desc
limit 10
