from pydantic import BaseModel

class UsuarioPW(BaseModel):
    id: int
    senha: str