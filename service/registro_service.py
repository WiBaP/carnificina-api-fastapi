from db.db import supabase
from fastapi.responses import JSONResponse

# =======================
# LISTAR TODOS
# =======================
def listar_registro_evento():
    result = supabase.table("registro_evento").select("*").execute()
    return result.data

def listar_registro_evento_por_evento(evento_id: int):
    result = supabase.table("registro_evento").select("*").eq("evento_id", evento_id).execute()
    return result.data

def listar_registro_evento_por_nick(nick: str):
    result = supabase.table("registro_evento").select("id, evento_id, nick, data_registro").eq("nick", nick).execute()
    return result.data

def listar_registro_evento_por_evento_e_nick(evento_id: int, nick: str):
    result = supabase.table("registro_evento").select("*").eq("evento_id", evento_id).eq("nick", nick).execute()
    return result.data

# =======================
# ADICIONAR REGISTRO
# =======================
def adicionar_registro_evento(evento_id: int, nick: str):
    # Checar se já existe
    existing = supabase.table("registro_evento").select("*").eq("evento_id", evento_id).eq("nick", nick).execute()
    if existing.data:
        return JSONResponse(content={"error": "Usuário já registrado neste evento"}, status_code=400)

    supabase.table("registro_evento").insert({"evento_id": evento_id, "nick": nick}).execute()
    return JSONResponse(content={"message": "Registro adicionado com sucesso"})

# =======================
# ATUALIZAR REGISTRO
# =======================
def atualizar_registro_evento(id: int, nick: str):
    result = supabase.table("registro_evento").update({"nick": nick}).eq("id", id).execute()
    if not result.data:
        return JSONResponse(content={"error": "Registro não encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Registro atualizado com sucesso"})

# =======================
# DELETAR REGISTRO
# =======================
def deletar_registro_evento(id: int):
    result = supabase.table("registro_evento").delete().eq("id", id).execute()
    if not result.data:
        return JSONResponse(content={"error": "Registro não encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Registro removido com sucesso"})

def deletar_registro_por_evento_e_nick(evento_id: int, nick: str):
    result = supabase.table("registro_evento").delete().eq("evento_id", evento_id).eq("nick", nick).execute()
    if not result.data:
        return JSONResponse(content={"error": "Registro não encontrado"}, status_code=404)
    return JSONResponse(content={"message": "Registro removido com sucesso"})
