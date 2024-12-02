import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, EndpointConnectionError

region_name = "us-east-1"  
bucket_name = "bucketdesafio-pedrosilva"  
csv_file = "tabela_desafio.csv"  
object_name = "tabela_desafio.csv"  

s3 = boto3.client(
    's3'
)

try:
    s3.upload_file(csv_file, bucket_name, object_name)
    print(f"Arquivo '{csv_file}' enviado para o bucket '{bucket_name}'.")

except EndpointConnectionError as e:
    print(f"Erro de conexão: {e}")
except NoCredentialsError:
    print("Credenciais ausentes ou incorretas!")
except PartialCredentialsError:
    print("Credenciais incompletas fornecidas!")
except Exception as e:
    print(f"Erro ao criar bucket ou fazer upload: {e}")

