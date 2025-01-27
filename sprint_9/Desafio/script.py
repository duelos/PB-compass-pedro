import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import functions as F

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

input_filmes_parquet = "s3://bucket-desafio-pedrosilva/Trusted/Movies/Parquet/2025/01/09/filmes.parquet"
input_json_filmes = "s3://bucket-desafio-pedrosilva/Trusted/TMDB/Parquet/2025/01/09/tmdb_json.parquet"
output_s3_path = "s3://bucket-desafio-pedrosilva/Refined/"

filmes_df = spark.read.parquet(input_filmes_parquet)
json_filmes_df = spark.read.json(input_json_filmes)

filmes_df = filmes_df.withColumnRenamed("id", "imdb_id")

dim_filme_df = json_filmes_df.select(
    "imdb_id",
    "original_title",
    "title"
)

dim_filme_df = dim_filme_df.join(
    filmes_df,
    on="imdb_id", 
    how="left"
).distinct()

dim_genero_df = json_filmes_df.select(
    F.explode(F.col("genres")).alias("genero")
).select(
    F.col("genero.id").alias("id_genero"),
    F.col("genero.name").alias("nome_genero")
).distinct()

dim_tempo_df = json_filmes_df.select(
    F.to_date("release_date").alias("data_lancamento")
).distinct()

dim_tempo_df = dim_tempo_df.withColumn("ano", F.year(F.col("data_lancamento")))\
    .withColumn("mes", F.month(F.col("data_lancamento")))\
    .withColumn("dia", F.dayofmonth(F.col("data_lancamento")))\
    .withColumn("dia_da_semana", F.date_format(F.col("data_lancamento"), "EEEE"))\
    .withColumn("id_tempo", F.monotonically_increasing_id())

fato_filmes_df = json_filmes_df.select(
    "imdb_id",
    "budget",
    "revenue",
    "popularity",
    "vote_average",
    "vote_count",
    "runtime",
    F.to_date("release_date").alias("data_lancamento")
)

fato_filmes_df = fato_filmes_df.join(dim_tempo_df, "data_lancamento", "left").join(
    dim_genero_df,
    fato_filmes_df["imdb_id"] == dim_genero_df["id_genero"],
    "left"
)

fato_filmes_df = fato_filmes_df.select(
    F.col("imdb_id").alias("id_filme"),
    "id_genero",
    "id_tempo",
    "budget",
    "revenue",
    "popularity",
    "vote_average",
    "vote_count",
    "runtime"
)

dim_filme_df.write.mode("overwrite").parquet(f"{output_s3_path}DimFilme/")
dim_genero_df.write.mode("overwrite").parquet(f"{output_s3_path}DimGenero/")
dim_tempo_df.write.mode("overwrite").parquet(f"{output_s3_path}DimTempo/")
fato_filmes_df.write.mode("overwrite").parquet(f"{output_s3_path}FatoFilmes/")

print("ETL concluído e tabelas salvas no S3!")