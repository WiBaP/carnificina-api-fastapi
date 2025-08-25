from sqlalchemy import create_engine, text
import os

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
DBNAME = os.environ.get("DBNAME")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1;"))
        for row in result:
            print("Test query result:", row)

        print("Connection successful!")
        print("USER:", USER)
        print("HOST:", HOST)
except Exception as e:
    print(f"Failed to connect: {e}")
