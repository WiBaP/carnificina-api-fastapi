from app import app
from controller import usuario_controller, evento_controller, registro_controller

@app.get("/")
def main():
    return {"mensagem": "API funcionando"}
