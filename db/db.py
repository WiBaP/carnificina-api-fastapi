# db.py
from sqlalchemy import create_engine, text
import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Carrega .env se estiver rodando localmente ---
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    logger.info(f".env carregado de {env_path}")
else:
    logger.info(".env não encontrado, usando variáveis de ambiente do sistema")

# --- Ler variáveis de ambiente ---
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT", "5432")  # padrão 5432 se não definido
DBNAME = os.environ.get("DBNAME")
sslmode="require"

logger.info(f"Tentando conectar ao banco com USER={USER}, HOST={HOST}, PORT={PORT}, DBNAME={DBNAME}")

# Converter PORT para inteiro
try:
    PORT = int(PORT)
except (TypeError, ValueError):
    logger.error(f"PORT inválida: {PORT}")
    raise

# --- Criar URL de conexão ---
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# --- Criar engine SQLAlchemy ---
engine = create_engine(DATABASE_URL)

# --- Testar conexão ---
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1;"))
        for row in result:
            logger.info(f"Teste de query retornou: {row}")
        logger.info("Conexão com o banco bem-sucedida!")
except Exception as e:
    logger.error("Erro na conexão com o banco:", exc_info=True)
    raise  # mantém o erro visível
