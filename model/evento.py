from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Evento(BaseModel):
    id: Optional[int] = None
    titulo: str = Field(..., max_length=50)
    descricao: Optional[str] = Field(None, max_length=1000)
    data_evento: datetime
    inicio_inscricao: datetime
    fim_inscricao: datetime
    status: str = "ativo"  # valores possíveis: "ativo", "finalizado"
    limite_participantes: Optional[int] = None