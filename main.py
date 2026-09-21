from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "mensagem": "Minha API está funcionando!"
    }


@app.get("/api/usuarios")
def listar_usuario():
    return {
        "id": 1,
        "nome": "João",
        "email": "joao@email.com"
    }

@app.post("/api/usuarios")
def criar_usuario(usuario: dict):
    return {
        "mensagem": "Usuário criado com sucesso",
        "usuario": usuario
    }
    
@app.get("api/v2/Pagamento/ConsultarStatusPedido?CodigoPedido={NumeroPedido}")
def listar_usuario():
    return {
		"success": true,
		"message": "Retorno Com Sucesso",
		"data": {
			"pedido": 123456,
			"status": "Pago Total"
		}
	}
