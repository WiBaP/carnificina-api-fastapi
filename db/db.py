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

# --- Ler a variável DATABASE_URL ---
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não encontrada nas variáveis de ambiente!")

logger.info(f"Tentando conectar usando DATABASE_URL={DATABASE_URL}")

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
    raise
