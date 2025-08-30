from db.db import engine
import bcrypt
from sqlalchemy import text

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
    with engine.connect() as conn:
        query = text("SELECT * FROM registro WHERE LOWER(nick) = :nick")
        row = conn.execute(query, {"nick": nick.lower()}).mappings().first()
        return row

def listar_usuarios():
    with engine.connect() as conn:
        query = text("SELECT * FROM registro")
        rows = conn.execute(query).mappings().all()
        return rows  # já retorna lista de dicionários

def cadastrar_usuario(nome, telefone, email, nick, classe, nivel, senha):
    with engine.connect() as conn:
        # 1. Validar senha
        if len(senha) < 4:
            return {"erro": "A senha deve ter no mínimo 4 caracteres."}

        # 2. Validar classe
        if classe.lower() not in CLASSES_VALIDAS:
            return {"erro": f"Classe inválida. As permitidas são: {', '.join(CLASSES_VALIDAS)}"}

        # 3. Verificar se email, telefone ou nick já existem
        for field, value in [("email", email), ("telefone", telefone), ("nick", nick)]:
            query = text(f"SELECT 1 FROM registro WHERE {field} = :value")
            if conn.execute(query, {"value": value}).fetchone():
                return {"erro": f"Já existe um usuário com este {field}."}

        # 4. Gerar hash da senha
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # 5. Inserir no banco
        query = text("""
            INSERT INTO registro (nome, telefone, email, nick, classe, nivel, senha)
            VALUES (:nome, :telefone, :email, :nick, :classe, :nivel, :senha)
        """)
        conn.execute(query, {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "nick": nick,
            "classe": classe.lower(),
            "nivel": nivel,
            "senha": senha_hash
        })
        conn.commit()

    return {"mensagem": "Usuário cadastrado com sucesso"}

def atualizar_usuario(id, nome, telefone, email, nick, classe, nivel, adm):
    """
    Atualiza os dados do usuário, mas NÃO altera a senha.
    """
    with engine.connect() as conn:
        query = text("""
            UPDATE registro 
            SET nome = :nome,
                telefone = :telefone,
                email = :email,
                nick = :nick,
                classe = :classe,
                nivel = :nivel,
                adm = :adm
            WHERE id = :id
        """)

        params = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "nick": nick,
            "classe": classe.lower(),
            "nivel": nivel,
            "adm": adm,
            "id": id
        }

        conn.execute(query, params)
        conn.commit()

    return {"mensagem": "Usuário atualizado com sucesso"}


def deletar_usuario(id):
    with engine.connect() as conn:
        query = text("DELETE FROM registro WHERE id = :id")
        conn.execute(query, {"id": id})
        conn.commit()
    return {"mensagem": "Usuário deletado com sucesso"}

def logar_usuario(nick: str, senha: str) -> bool:
    usuario = get_usuario_por_nick(nick)
    if not usuario:
        return False
    senha_hash = usuario["senha"]
    return bcrypt.checkpw(senha.encode("utf-8"), senha_hash.encode("utf-8"))

def alterar_senha(id, senha):
    
    senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    
    with engine.connect() as conn:
        query = text("UPDATE registro SET senha = :senha WHERE id = :id")
        conn.execute(query, {"senha": senha_hash, "id": id})
        conn.commit()
    
    return {"mensagem": "Senha alterada com sucesso"}

