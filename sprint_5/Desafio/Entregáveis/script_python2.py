import boto3
import pandas as pd
from io import StringIO

s3_client = boto3.client('s3', region_name='us-east-1') 

bucket_name = 'bucketdesafio-pedrosilva'  
object_key = 'tabela_desafio.csv'

response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
csv_content = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_content))

# 1. Filtrar dados usando 2 operadores lógicos
# Filtrando registros onde UF é 'SP' e AMBIENTE é 'Natural'
filtro = (df['UF'] == 'SP') & (df['AMBIENTE'] == 1)
df_filtrado = df[filtro]

print("Registros filtrados (UF = 'SP' e AMBIENTE = 1):")
print(df_filtrado)
print('-'*20)

# 2. Funções de agregação
# Contagem do número de registros por "ENTIDADE_RESPONSAVEL"
df_agregado = df.groupby('ENTIDADE_RESPONSAVEL').agg({'OBJECTID': 'count'})
print('Contagem:')                                                    
print(df_agregado)
print('-'*20)
# 3. Função condicional
# Criar uma nova coluna "STATUS" que indica 'Mediano' se "AMBIENTE" for '1', caso contrário 'Abaixo da média'
df['STATUS'] = df['AMBIENTE'].apply(lambda x: 'Mediano' if x == 1 else 'Abaixo da média')
print('Status:')
print(df[['AMBIENTE', 'STATUS']])
print('-'*20)
# 4. Função de conversão
# Converter "X" e "Y" para tipo inteiro
df['X'] = df['X'].astype(int)
df['Y'] = df['Y'].astype(int)
print("\nConversão de tipo:")
print(df[['X', 'Y']].dtypes)
print('-'*20)
# 5. Função de data
df['ANO'] = pd.to_datetime(df['ANO'], format='%Y')  
print("\nFunção de data aplicada:")
print(df['ANO'])
print('-'*20)
# 6. Função de String
# Criar uma coluna "CORPO_DAGUA" em maiúsculas
df['CORPO_DAGUA'] = df['CORPO_DAGUA'].str.upper()
print("\nFunção de string aplicada:")
print(df[['CORPO_DAGUA']])

# Convertendo e enviando para o bucket

s3_client = boto3.client('s3', region_name='us-east-1') 
bucket_name = 'bucketdesafio-pedrosilva'
object_key = 'tabela_desafio.csv'

response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
csv_content = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_content))
