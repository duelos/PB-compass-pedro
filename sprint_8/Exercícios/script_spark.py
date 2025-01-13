from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when, col, udf, expr
from sprint_8.Exercícios.script_spark import SparkContext, SQLContext
from pyspark.sql.types import StringType, IntegerType
import random
spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

df_nomes.show(5)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")

df_nomes.show(10)

df_nomes = df_nomes.withColumn("random", rand())

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(col("random") < 0.33, "Fundamental")
    .when(col("random") < 0.66, "Medio")
    .otherwise("Superior")
)

df_nomes = df_nomes.drop("random")

df_nomes.show(10)

paises = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia",
    "Equador", "Guiana", "Paraguai", "Peru", "Suriname",
    "Uruguai", "Venezuela", "Guiana Francesa"
]

def pais_aleatorio():
    return random.choice(paises)

pais_udf = udf(pais_aleatorio, StringType())

df_nomes = df_nomes.withColumn("Pais", pais_udf())

df_nomes.show(10)

df_nomes = df_nomes.withColumn("AnoNascimento", 
    (1945 + (rand() * (2010 - 1945)).cast("int"))
)

df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000).select("Nome")

df_select.show(10)

df_nomes.createOrReplaceTempView ("pessoas")

spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show()

df_millenials = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994))

df_millenials_count = df_millenials.count()

print(f"Quantidade de millennials: {df_millenials_count}")

df_nomes.createOrReplaceTempView("pessoas")

millenials_count = spark.sql("""
    SELECT COUNT(*) AS quantidade_millenials
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""")

millenials_count.show()

df_nomes.createOrReplaceTempView("pessoas")

geracoes_query = """
    SELECT
        Pais,
        CASE
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
            ELSE 'Outros'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1944 AND 2015
    GROUP BY Pais, Geracao
    ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
"""

df_geracoes = spark.sql(geracoes_query)

df_geracoes.show(100)

