# pipeline_cripto.py
# Pipeline ETL para dados de criptomoedas - Extrai, Transforma e Carrega dados de API para MySQL

import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import os

# CONFIGURAÇÕES DA API
API_URL = "https://api.coingecko.com/api/v3/simple/price"
params = {
    'ids': 'bitcoin,ethereum,cardano,solana',
    'vs_currencies': 'usd,brl',
    'include_last_updated_at': 'true'
}

# CONFIGURAÇÕES DO BANCO DE DADOS
DB_USER = 'root'
DB_PASSWORD = 'sua_senha_aqui'  # 👈 Substitua pela sua senha real
DB_HOST = 'localhost'
DB_NAME = 'cripto2_db'
DB_CONNECTION_STRING = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# ETAPA 1: EXTRAÇÃO - Coleta dados da API CoinGecko
print("Coletando dados da API CoinGecko...")
try:
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    dados_brutos = response.json()
    print("✅ Dados extraídos com sucesso")
except requests.exceptions.RequestException as e:
    print(f"❌ Falha na requisição: {e}")
    exit()

# ETAPA 2: TRANSFORMAÇÃO - Estrutura os dados para armazenamento
print("Processando e estruturando dados...")
dados_transformados = []

# Converte resposta JSON em estrutura tabular
for moeda, info in dados_brutos.items():
    registro = {
        'moeda': moeda.capitalize(),
        'preco_usd': info['usd'],
        'preco_brl': info['brl'],
        'timestamp_registro': datetime.fromtimestamp(info['last_updated_at'])
    }
    dados_transformados.append(registro)

df = pd.DataFrame(dados_transformados)
print("Dados transformados:")
print(df)

# ETAPA 3: CARGA - Armazena dados nos destinos
print("Iniciando carga de dados...")

# Backup em arquivo CSV com timestamp para versionamento
nome_arquivo = f"precos_cripto_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
df.to_csv(nome_arquivo, index=False)
print(f"✅ Backup CSV salvo: {nome_arquivo}")

# Conexão e carga no MySQL
try:
    engine = create_engine(DB_CONNECTION_STRING)

    with engine.connect() as connection:
        # Cria tabela se não existir - usando DECIMAL para precisão monetária
        create_table_query = text("""
            CREATE TABLE IF NOT EXISTS precos_cripto (
                id INT AUTO_INCREMENT PRIMARY KEY,
                moeda VARCHAR(50) NOT NULL,
                preco_usd DECIMAL(18, 6) NOT NULL,
                preco_brl DECIMAL(18, 6) NOT NULL,
                timestamp_registro TIMESTAMP
            )
        """)
        connection.execute(create_table_query)
        connection.commit()

        # Insere dados mantendo histórico existente
        df.to_sql('precos_cripto', con=connection, if_exists='append', index=False)
        connection.commit()

    print("✅ Dados carregados no MySQL com sucesso")

except Exception as e:
    print(f"❌ Erro na conexão com MySQL: {e}")

print("🎉 Pipeline executado com sucesso!")