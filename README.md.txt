# 📊 Pipeline ETL de Dados de Criptomoedas

Pipeline de dados que extrai, transforma e carrega cotações de criptomoedas em tempo real para um banco de dados MySQL.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Pandas** - Manipulação e transformação de dados
- **Requests** - Integração com API CoinGecko
- **SQLAlchemy** - Conexão com banco de dados MySQL
- **MySQL** - Armazenamento dos dados

## ⚠️ Configuração Necessária

Antes de executar o script:

1. Abra o arquivo `pipeline_cripto.py`
2. Localize a seção **CONFIGURAÇÕES DO BANCO DE DADOS**
3. Substitua os valores placeholders pelas suas credenciais:
   - `DB_USER = 'seu_usuario_mysql'`
   - `DB_PASSWORD = 'sua_senha_mysql'`

## 🚀 Como Executar

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar o pipeline
python pipeline_cripto.py