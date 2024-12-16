WITH periodo AS (
    SELECT DISTINCT
        FLOOR(Ano / 10) * 10 AS periodo, 
        Nome, 
        SUM(Total) AS TotalPorNome
    FROM meubanco.tabela
    WHERE Ano >= 1950
    GROUP BY FLOOR(Ano / 10) * 10, Nome
)
SELECT periodo, Nome, TotalPorNome
FROM (
    SELECT 
        periodo, 
        Nome, 
        TotalPorNome,
        ROW_NUMBER() OVER (PARTITION BY periodo ORDER BY TotalPorNome DESC) AS Rank
    FROM periodo
) AS RankedData
WHERE Rank <= 3
ORDER BY periodo asc, Rank;

