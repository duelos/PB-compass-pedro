import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'SOURCE_BUCKET', 'TARGET_BUCKET', 'JSON_KEY', 'PARQUET_KEY'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_bucket = args['SOURCE_BUCKET']  
target_bucket = args['TARGET_BUCKET'] 
json_key = args['JSON_KEY'] 
parquet_key = args['PARQUET_KEY']  

json_path = f"s3://bucket-desafio-pedrosilva/Raw/TMDB/JSON/2025/1/21/filmes_detalhados_tmdb.json"
parquet_path = f"s3://bucket-desafio-pedrosilva/Trusted/TMDB/Parquet/2025/01/09/"

dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [json_path]},
    format="json"
)

data_frame = dynamic_frame.toDF()

data_frame.write.mode("overwrite").parquet(parquet_path)

job.commit()
