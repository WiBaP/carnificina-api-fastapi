from db.db import engine
from fastapi.responses import JSONResponse
from sqlalchemy import text

# =======================
# LISTAR TODOS
# =======================
def listar_registro_evento():
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT * FROM registro_evento")).mappings().all()
        return rows  # já retorna lista de dicionários

def listar_registro_evento_por_evento(evento_id: int):
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT * FROM registro_evento WHERE evento_id = :evento_id"),
            {"evento_id": evento_id}
        ).mappings().all()
        return rows

def listar_registro_evento_por_nick(nick: str):
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT id, evento_id, nick, data_registro FROM registro_evento WHERE nick = :nick"),
            {"nick": nick}
        ).mappings().all()
        return rows

def listar_registro_evento_por_evento_e_nick(evento_id: int, nick: str):
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT * FROM registro_evento WHERE evento_id = :evento_id AND nick = :nick"),
            {"evento_id": evento_id, "nick": nick}
        ).mappings().all()
        return rows

# =======================
# ADICIONAR REGISTRO
# =======================
def adicionar_registro_evento(evento_id: int, nick: str):
    with engine.begin() as conn:
        # Checar se já existe
        existing = conn.execute(
            text("SELECT 1 FROM registro_evento WHERE evento_id = :evento_id AND nick = :nick"),
            {"evento_id": evento_id, "nick": nick}
        ).first()
        if existing:
            return JSONResponse(
                content={"error": "Usuário já registrado neste evento"},
                status_code=400
            )
        conn.execute(
            text("INSERT INTO registro_evento (evento_id, nick) VALUES (:evento_id, :nick)"),
            {"evento_id": evento_id, "nick": nick}
        )
    return JSONResponse(content={"message": "Registro adicionado com sucesso"})

# =======================
# ATUALIZAR REGISTRO
# =======================
def atualizar_registro_evento(id: int, nick: str):
    with engine.begin() as conn:
        result = conn.execute(
            text("UPDATE registro_evento SET nick = :nick WHERE id = :id"),
            {"nick": nick, "id": id}
        )
        if result.rowcount == 0:
            return JSONResponse(content={"error": "Registro não encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Registro atualizado com sucesso"})

# =======================
# DELETAR REGISTRO
# =======================
def deletar_registro_evento(id: int):
    with engine.begin() as conn:
        result = conn.execute(
            text("DELETE FROM registro_evento WHERE id = :id"),
            {"id": id}
        )
        if result.rowcount == 0:
            return JSONResponse(content={"error": "Registro não encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Registro removido com sucesso"})

def deletar_registro_por_evento_e_nick(evento_id: int, nick: str):
    with engine.begin() as conn:
        result = conn.execute(
            text("DELETE FROM registro_evento WHERE evento_id = :evento_id AND nick = :nick"),
            {"evento_id": evento_id, "nick": nick}
        )
        if result.rowcount == 0:
            return JSONResponse(content={"error": "Registro não encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Registro removido com sucesso"})