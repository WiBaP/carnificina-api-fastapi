from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str = Field(..., max_length=50)
    telefone: str = Field(..., max_length=30)
    email: str = Field(..., max_length=50)
    nick: str = Field(..., max_length=50)
    classe: str = Field(..., max_length=15)
    nivel: str = Field(..., max_length=15)
    senha: str = Field(..., max_length=255)
    data_confirmacao: Optional[datetime] = None
    adm: Optional[bool] = None
