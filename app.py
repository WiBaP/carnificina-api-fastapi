from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # De onde aceitar requisições ("*" = qualquer site)
    allow_credentials=True,    # Permite enviar cookies/autenticação
    allow_methods=["*"],       # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],       # Permite todos os headers
)