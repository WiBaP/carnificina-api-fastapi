from fastapi import HTTPException
from app import app
from service.evento_service import listar_evento, cadastrar_evento, deletar_evento, atualizar_evento
from model.evento import Evento
from model.evento_id import EventoID

@app.get("/listar-evento")
def listar():
    return listar_evento()

@app.post("/cadastrar-evento")
def cadastrar(evento: Evento):
    return cadastrar_evento(
        evento.titulo,
        evento.descricao,
        evento.data_evento,
        evento.inicio_inscricao,
        evento.fim_inscricao,
        evento.status,
        evento.limite_participantes

    )

@app.put("/atualizar-evento")
def atualizar(evento: Evento):
    return atualizar_evento(
        evento.id,
        evento.titulo,
        evento.descricao,
        evento.data_evento,
        evento.inicio_inscricao,
        evento.fim_inscricao,
        evento.status,
        evento.limite_participantes
    )

@app.delete("/deletar-evento/{id}")
def deletar(id: int):
    try:
        return deletar_evento(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
