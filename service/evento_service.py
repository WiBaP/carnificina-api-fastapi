from db.db import engine
from fastapi.responses import JSONResponse
from sqlalchemy import text


def listar_evento():
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT * FROM evento")).mappings().all()
        return rows

def cadastrar_evento(titulo, descricao, data_evento, inicio_inscricao, fim_inscricao, status="ativo", limite_participantes=None):
    try:
        with engine.begin() as conn:  # begin() faz commit automático
            conn.execute(
                text("""
                    INSERT INTO evento (titulo, descricao, data_evento, inicio_inscricao, fim_inscricao, status, limite_participantes)
                    VALUES (:titulo, :descricao, :data_evento, :inicio_inscricao, :fim_inscricao, :status, :limite_participantes)
                """),
                {
                    "titulo": titulo,
                    "descricao": descricao,
                    "data_evento": data_evento,
                    "inicio_inscricao": inicio_inscricao,
                    "fim_inscricao": fim_inscricao,
                    "status": status,
                    "limite_participantes": limite_participantes
                }
            )
        return JSONResponse(content={"mensagem": "Evento cadastrado com sucesso!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})

def atualizar_evento(id, titulo, descricao, data_evento, inicio_inscricao, fim_inscricao, status, limite_participantes=None):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    UPDATE evento
                    SET titulo = :titulo,
                        descricao = :descricao,
                        data_evento = :data_evento,
                        inicio_inscricao = :inicio_inscricao,
                        fim_inscricao = :fim_inscricao,
                        status = :status,
                        limite_participantes = :limite_participantes
                    WHERE id = :id
                """),
                {
                    "titulo": titulo,
                    "descricao": descricao,
                    "data_evento": data_evento,
                    "inicio_inscricao": inicio_inscricao,
                    "fim_inscricao": fim_inscricao,
                    "status": status,
                    "limite_participantes": limite_participantes,
                    "id": id
                }
            )
            if result.rowcount == 0:
                return JSONResponse(content={"erro": "Evento não encontrado"}, status_code=404)
        return JSONResponse(content={"mensagem": "Evento atualizado com sucesso!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})

def deletar_evento(id):
    try:
        with engine.begin() as conn:
            result = conn.execute(
                text("DELETE FROM evento WHERE id = :id"),
                {"id": id}
            )
            if result.rowcount == 0:
                return JSONResponse(content={"erro": "Evento não encontrado"}, status_code=404)
        return JSONResponse(content={"mensagem": "Evento deletado com sucesso!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
