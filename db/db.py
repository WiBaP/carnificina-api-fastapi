from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Carrega .env da raiz do projeto
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))  # ⬅️ converter para int aqui
DBNAME = os.getenv("DBNAME")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

engine = create_engine(DATABASE_URL)
