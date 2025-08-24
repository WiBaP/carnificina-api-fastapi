from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class RegistroEventoBase(BaseModel):
    id: Optional[int] = None
    evento_id: int
    nick: str
    data_registro: Optional[datetime] = None

