import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper, count, desc

args = getResolvedOptions(
    sys.argv, 
    ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH']
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_OUTPUT_PATH']


df = spark.read.options(header=True, inferSchema=True).csv(source_file)

print("Schema do DataFrame:")
df.printSchema()

df_upper = df.withColumn("nome", upper(col("nome")))

linha_count = df_upper.count()
print(f"Total de linhas no DataFrame: {linha_count}")

df_grouped = (
    df_upper.groupBy("ano", "sexo")
    .agg(count("nome").alias("contagem_nomes"))
    .orderBy(desc("ano"))
)
print("Contagem de nomes agrupados por ano e sexo:")
df_grouped.show()

feminino_top = (
    df_upper.filter(col("sexo") == "F")
    .groupBy("ano", "nome")
    .agg(count("nome").alias("contagem"))
    .orderBy(desc("contagem"))
    .first()
)
print(f"Nome feminino mais registrado: {feminino_top['nome']} em {feminino_top['ano']}")

masculino_top = (
    df_upper.filter(col("sexo") == "M")
    .groupBy("ano", "nome")
    .agg(count("nome").alias("contagem"))
    .orderBy(desc("contagem"))
    .first()
)
print(f"Nome masculino mais registrado: {masculino_top['nome']} em {masculino_top['ano']}")

registros_por_ano = (
    df_upper.groupBy("ano")
    .agg(count("*").alias("total_registros"))
    .orderBy("ano")
    .limit(10)
)
print("Total de registros (masculinos e femininos) por ano (primeiras 10 linhas):")
registros_por_ano.show()

df_upper.write.mode("overwrite").partitionBy("sexo", "ano").json(target_path)

print(f"DataFrame gravado com sucesso no path: {target_path}")


job.commit()
