import requests
import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datetime import datetime
import os

TMDB_API_KEY = os.environ['chave_tmdb']
BUCKET_NAME = "bucket-desafio-pedrosilva"

s3_client = boto3.client('s3')

filmes_imdb_ids = [
    "tt0004974", "tt0005615", "tt0006333", "tt0006820", "tt0008100",
    "tt0008565", "t0008825", "tt0008826", "tt0010600", "tt0011130",
    "tt0012456", "tt0013367", "tt0014391", "tt0015051", "tt0016039",
    "tt0016237", "tt0016338", "tt0017136", "tt0018584", "tt0020198", 
    "tt0816692"
]

def buscar_detalhes_tmdb(id_imdb):
    url_find = f"https://api.themoviedb.org/3/find/{id_imdb}"
    params = {
        "api_key": TMDB_API_KEY,
        "external_source": "imdb_id"
    }
    response = requests.get(url_find, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['movie_results']:
            return data['movie_results'][0]
    return None

def lambda_handler(event, context):
    try:
        dados_filmes = []
        for imdb_id in filmes_imdb_ids:
            detalhes = buscar_detalhes_tmdb(imdb_id)
            if detalhes:
                dados_filmes.append(detalhes)

        arquivo_json = json.dumps(dados_filmes, indent=4)
        
        data_atual = datetime.now()
        caminho_s3 = f"Raw/TMDB/JSON/{data_atual.year}/{data_atual.day}/{data_atual.month}/filmes_tmdb.json"

        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=caminho_s3,
            Body=arquivo_json,
            ContentType='application/json'
        )
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Arquivo salvo com sucesso em s3://{BUCKET_NAME}/{caminho_s3}",
                "file_path": caminho_s3
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Erro ao processar a requisição",
                "error": str(e)
            })
        }

