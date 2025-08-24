from service.usuario_service import listar_usuarios, cadastrar_usuario, atualizar_usuario, deletar_usuario, logar_usuario, get_usuario_por_nick
from app import app
from model.usuario import Usuario
from model.usuario_id import UsuarioID
from model.usuario_login import UsuarioLogin
from fastapi import HTTPException

@app.get("/usuario/{nick}")
def listar_por_nick(nick: str):
    usuario = get_usuario_por_nick(nick)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@app.get("/listar-usuario")
def listar():
    return listar_usuarios()

@app.post("/cadastrar-usuario")
def cadastrar(usuario: Usuario):
    return cadastrar_usuario(
        usuario.nome,
        usuario.telefone,
        usuario.email,
        usuario.nick,
        usuario.classe,
        usuario.nivel,
        usuario.senha
    )

@app.put("/atualizar-usuario")
def atualizar(usuario: Usuario):
    return atualizar_usuario(
        usuario.id,
        usuario.nome,
        usuario.telefone,
        usuario.email,
        usuario.nick,
        usuario.classe,
        usuario.nivel,
        usuario.senha,
        usuario.adm
    )

@app.delete("/deletar-usuario")
def deletar(usuario: UsuarioID):
    return deletar_usuario(usuario.id)
    
@app.post("/logar-usuario")
def logar(usuario: UsuarioLogin):
    sucesso = logar_usuario(usuario.nick, usuario.senha)
    
    if sucesso:
        return {"mensagem": "Login realizado com sucesso!"}
    else:
        return {"mensagem": "Usuário ou senha inválidos"}
