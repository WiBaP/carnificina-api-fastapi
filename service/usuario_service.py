from db.db import supabase
import bcrypt

# lista de classes válidas
CLASSES_VALIDAS = {
    "assassin",
    "fighter",
    "knight",
    "atalanta",
    "archer",
    "pikeman",
    "mechanician",
    "magician",
    "shaman",
    "priestess"
}

def get_usuario_por_nick(nick: str):
    response = supabase.table("registro").select("*").eq("nick", nick).execute()
    if response.data:
        return response.data[0]
    return None

def listar_usuarios():
    response = supabase.table("registro").select("*").execute()
    return response.data

def cadastrar_usuario(nome, telefone, email, nick, classe, nivel, senha):
    # 1. Validar senha
    if len(senha) < 4:
        return {"erro": "A senha deve ter no mínimo 4 caracteres."}

    # 2. Validar classe
    if classe.lower() not in CLASSES_VALIDAS:
        return {"erro": f"Classe inválida. As permitidas são: {', '.join(CLASSES_VALIDAS)}"}

    # 3. Verificar se email, telefone ou nick já existem
    for field, value in [("email", email), ("telefone", telefone), ("nick", nick)]:
        existing = supabase.table("registro").select("id").eq(field, value).execute()
        if existing.data:
            return {"erro": f"Já existe um usuário com este {field}."}

    # 4. Gerar hash da senha
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # 5. Inserir no banco
    supabase.table("registro").insert({
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "nick": nick,
        "classe": classe.lower(),
        "nivel": nivel,
        "senha": senha_hash
    }).execute()

    return {"mensagem": "Usuário cadastrado com sucesso"}

def atualizar_usuario(id, nome, telefone, email, nick, classe, nivel, senha, adm):
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    supabase.table("registro").update({
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "nick": nick,
        "classe": classe.lower(),
        "nivel": nivel,
        "senha": senha_hash,
        "adm": adm
    }).eq("id", id).execute()

    return {"mensagem": "Usuário atualizado com sucesso"}

def deletar_usuario(id):
    supabase.table("registro").delete().eq("id", id).execute()
    return {"mensagem": "Usuário deletado com sucesso"}

def logar_usuario(nick, senha):
    usuario = get_usuario_por_nick(nick)
    if not usuario:
        return False
    senha_hash = usuario["senha"]
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))
