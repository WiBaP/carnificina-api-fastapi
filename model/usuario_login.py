from pydantic import BaseModel, Field

class UsuarioLogin(BaseModel):
    nick: str = Field(..., max_length=50)
    senha: str = Field(..., max_length=255)