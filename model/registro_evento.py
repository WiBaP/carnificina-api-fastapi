from pydantic import BaseModel
from typing import Optional

class RegistroEvento(BaseModel):
    id: Optional[int] = None
    evento_id: int
    nick: str
