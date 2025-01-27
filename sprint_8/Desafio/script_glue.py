from awsglue.transforms import *
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

source_path = "s3://bucket-desafio-pedrosilva/Raw/Local/CSV/Series/2024/12/13/series.csv"
destination_path = "s3://bucket-desafio-pedrosilva/Trusted/Parquet/Series/2025/01/09/"

csv_data = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_path]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}  
)

csv_data.printSchema()

if csv_data.count() == 0:
    sys.exit(0)

csv_data.show()

glueContext.write_dynamic_frame.from_options(
    frame=csv_data,
    connection_type="s3",
    connection_options={"path": destination_path},
    format="parquet"
)
