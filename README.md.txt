# Pipeline ETL de Dados de Criptomoedas

Script Python que extrai, transforma e carrega cotações de criptomoedas da API CoinGecko para um banco de dados MySQL.

## Tecnologias Utilizadas

- Python 3
- Pandas
- Requests
- SQLAlchemy
- MySQL

## Como Executar

1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o script: `python pipeline_cripto.py`

## ⚠️ Configuração e Segurança

Antes de executar o script, **configure suas credenciais do MySQL**:

1. Abra o arquivo `pipeline_cripto.py`
2. Localize a seção `CONFIGURAÇÕES DO BANCO DE DADOS`
3. Substitua os valores placeholders pelas suas credenciais reais:
   - `DB_USER = 'seu_usuario'`
   - `DB_PASSWORD = 'sua_senha_real'`