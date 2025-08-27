from db.db import supabase
from fastapi.responses import JSONResponse


# =======================
# LISTAR EVENTOS
# =======================
def listar_evento():
    result = supabase.table("evento").select("*").execute()
    return result.data


# =======================
# CADASTRAR EVENTO
# =======================
def cadastrar_evento(titulo, descricao, data_evento, inicio_inscricao, fim_inscricao, status="ativo", limite_participantes=None):
    try:
        supabase.table("evento").insert({
            "titulo": titulo,
            "descricao": descricao,
            "data_evento": data_evento,
            "inicio_inscricao": inicio_inscricao,
            "fim_inscricao": fim_inscricao,
            "status": status,
            "limite_participantes": limite_participantes
        }).execute()

        return JSONResponse(content={"mensagem": "Evento cadastrado com sucesso!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})


# =======================
# ATUALIZAR EVENTO
# =======================
def atualizar_evento(id, titulo, descricao, data_evento, inicio_inscricao, fim_inscricao, status, limite_participantes=None):
    try:
        result = supabase.table("evento").update({
            "titulo": titulo,
            "descricao": descricao,
            "data_evento": data_evento,
            "inicio_inscricao": inicio_inscricao,
            "fim_inscricao": fim_inscricao,
            "status": status,
            "limite_participantes": limite_participantes
        }).eq("id", id).execute()

        if not result.data:
            return JSONResponse(content={"erro": "Evento não encontrado"}, status_code=404)

        return JSONResponse(content={"mensagem": "Evento atualizado com sucesso!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})


# =======================
# DELETAR EVENTO
# =======================
def deletar_evento(id):
    try:
        result = supabase.table("evento").delete().eq("id", id).execute()

        if not result.data:
            return JSONResponse(content={"erro": "Evento não encontrado"}, status_code=404)

        return JSONResponse(content={"mensagem": "Evento deletado com sucesso!"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
