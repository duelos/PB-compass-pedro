import requests
import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datetime import datetime

TMDB_API_KEY = "2fffba7c58b02b4b8da8ffef87932965"
BUCKET_NAME = "bucket-desafio-pedrosilva"

s3_client = boto3.client('s3')

filmes_imdb_ids = [
    "tt0131597","tt0212712","tt0270841","tt0270846","tt0289879","tt0296572","tt0307343","tt0307922","tt0308281","tt0311462","tt0314063","tt0316654","tt0318627","tt0319262","tt0321626","tt0325596","tt0327162","tt0330175","tt0330313","tt0338013","tt0343818","tt0344777","tt0345777","tt0346811","tt0347534","tt0349047","tt0350061","tt0356618","tt0357585","tt0357894","tt0359013","tt0361679","tt0362942","tt0363623","tt0364343","tt0364726","tt0366985","tt0367677","tt0368008","tt0371282","tt0371920","tt0372851","tt0377713","tt0384116","tt0385635","tt0385990","tt0388349","tt0388556","tt0390384","tt0390463","tt0392789","tt0395932","tt0398075","tt0399134","tt0404325","tt0404337","tt0404745","tt0405821","tt0407695","tt0409860"
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
            return data['movie_results'][0]['id']  
    return None

def buscar_info_completa_tmdb(id_tmdb):
    
    url_movie = f"https://api.themoviedb.org/3/movie/{id_tmdb}"
    params = {"api_key": TMDB_API_KEY, "append_to_response": "credits,release_dates"}
    response = requests.get(url_movie, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def lambda_handler(event, context):
    try:
        dados_filmes = []
        for imdb_id in filmes_imdb_ids:
            id_tmdb = buscar_detalhes_tmdb(imdb_id)
            if id_tmdb:
                detalhes_completos = buscar_info_completa_tmdb(id_tmdb)
                if detalhes_completos:
                    dados_filmes.append(detalhes_completos)

        
        arquivo_json = json.dumps(dados_filmes, indent=4)
        
        data_atual = datetime.now()
        caminho_s3 = f"Raw/TMDB/JSON/{data_atual.year}/{data_atual.month}/{data_atual.day}/filmes_detalhados_tmdb.json"

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
