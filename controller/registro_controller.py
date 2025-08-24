from fastapi import HTTPException
from app import app

from service.registro_service import (
    listar_registro_evento,
    listar_registro_evento_por_evento,
    adicionar_registro_evento,
    atualizar_registro_evento,
    deletar_registro_evento,
    deletar_registro_por_evento_e_nick
)
from model.registro_evento import RegistroEvento
from model.registro_evento_id import RegistroEventoID


@app.get("/listar-registro-evento")
def listar():
    return listar_registro_evento()

@app.get("/listar-registro-evento/{evento_id}")
def listar_por_evento(evento_id: int):
    return listar_registro_evento_por_evento(evento_id)

@app.get("/listar-registro-evento-nick/{nick}")
def listar_por_nick(id: int, evento_id:int, nick: str):
    from service.registro_service import listar_registro_evento_por_nick
    return listar_registro_evento_por_nick(nick)

@app.get("/listar-registro-evento/{evento_id}/{nick}")
def listar_por_evento_e_nick(evento_id: int, nick: str):
    registros = listar_registro_evento_por_evento(evento_id)
    # acessando como dict
    return [r for r in registros if r["nick"] == nick]

@app.post("/adicionar-registro-evento")
def adicionar(registro: RegistroEvento):
    try:
        return adicionar_registro_evento(registro.evento_id, registro.nick)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/atualizar-registro-evento")
def atualizar(registro: RegistroEvento):
    try:
        return atualizar_registro_evento(registro.id, registro.nick)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/deletar-registro-evento/id/{id}")
def deletar(id: int):
    try:
        return deletar_registro_evento(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/deletar-registro-evento/{evento_id}/{nick}")
def deletar_por_evento_e_nick(evento_id: int, nick: str):
    try:
        return deletar_registro_por_evento_e_nick(evento_id, nick)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))   
