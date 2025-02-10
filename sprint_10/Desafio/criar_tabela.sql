CREATE TABLE desafio_filmes AS
SELECT 
    fi.original_title,
    f.id_filme, 
    f.budget, 
    f.revenue, 
    f.popularity, 
    f.vote_average, 
    f.vote_count, 
    f.runtime,
    g.nome_genero,
    t.ano,
    t.mes
FROM fatofilmes f
LEFT JOIN dimgenero g ON CAST(f.id_genero AS VARCHAR) = g.id_genero
LEFT JOIN dimtempo t ON f.id_tempo = t.id_tempo
LEFT JOIN dimfilme fi ON f.id_filme = imdb_id;
