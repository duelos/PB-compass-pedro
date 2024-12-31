import csv
import boto3

arquivo1 = "/app/dados/movies.csv"
arquivo2 = "/app/dados/series.csv"

def ler_csv(caminho):
    with open(caminho, 'r', encoding='utf-8') as file:
        leitor = csv.reader(file)
        for _ in leitor:
            pass 

ler_csv(arquivo1)
ler_csv(arquivo2)

print("Arquivos lidos com sucesso!")

# ENVIANDO OS ARQUIVOS

region_name = "us-east-1"  
bucket_name = "bucket-desafio-pedrosilva"  

csv_file = '/home/pedro/Downloads/Filmes_e_Series/movies.csv' 
object_name = "Raw/Local/CSV/Movies/2024/12/13/movies.csv"  

csv_file2 = '/home/pedro/Downloads/Filmes_e_Series/series.csv' 
object_name2 = "Raw/Local/CSV/Series/2024/12/13/series.csv"  

s3 = boto3.client(
    's3'
)

s3.upload_file(arquivo1, bucket_name, object_name)
print(f"Arquivo '{arquivo1}' enviado para o bucket '{bucket_name}'.")

s3.upload_file(arquivo2, bucket_name, object_name2)
print(f"Arquivo '{arquivo2}' enviado para o bucket '{bucket_name}'.")
