from fastapi import FastAPI, HTTPException

app = FastAPI()

#127.0.0.1:46764 - "GET /favicon.ico HTTP/1.1" 404 Not Found
#Eliminando mensagem
@app.get("/favicon.ico")
def favicon():
    return {}
    

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
    
@app.get("api/v2/Pagamento/Callback?CodigoParceiro={CodigoParceiro}")
def consultar_pedido():
    return {
		"success": True,
		"message": "Retorno Com Sucesso",
		"data": {
			"pedido": 123456,
			"status": "Pago Total",
			"valorTotal": 8029.42
		}
	}
	
@app.get("/api/v2/Pagamento/Callback")
def consultar_status_pedido(CodigoParceiro: int):

    pedidos = {
        123456: "Pago Total",
		129805: "Pago Total",
		129810: "Pago Total",
		129826: "Pago Total",
		129974: "Pago Total",
		130000: "Pago Total",
        170091: "Consulta - Pedido sem transação válida",
        100000: "Teste",
		100001: "Cancelado",
        100002: "Em análise",
        999999: "Consulta - Pedido sem transação válida"
    }
    
    if CodigoParceiro not in pedidos:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )
	
    return {
		"success": True,
		"message": "Retorno Com Sucesso",
		"data": {
			"pedido": CodigoParceiro,
			"status": pedidos[CodigoParceiro],
			"valorTotal": 8029.42
		}
	}