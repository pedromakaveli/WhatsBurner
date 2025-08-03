from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.post("/envia_mensagem")

async def recieve_and_send_message (request: Request):
    message_from = None
    message_to = None
    message = None
    url_client = None

    # Abaixo deve conter a requisição apontando para o client correto
    # O endpoint deve ser: /recebe_mensagem_servidor