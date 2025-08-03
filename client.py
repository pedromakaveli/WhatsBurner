from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import random
import requests


app = FastAPI()

@app.post("/recebe_mensagem_servidor")
async def recebe_e_responde_mensagem (request: Request):
    '''
    Será necessário buscar o índice da mensagem
    no arquivo .env e enviar a resposta dessa mensagem
    baseado em seu índice

    Essa função deve chamar o endpoint de enviar mensagem da Evolution API
    '''
    
    body = {

    }

    re = None

@app.post("/envia_mensagem_para_servidor")

async def envia_mensagem (request: Request):
    '''
    Essa URL é acessada apenas na inicialização do arquivo main
    para disparar a primeira mensagem

    Primeiro será necessário enviar a mensagem para
    a API da Evolution API, utilizando o endpoint send message
    Depois, deve-se fazer uma requisição para o client
    para que ele receba a mensagem e possa responder
    
    '''
    re = await request.json()

    my_client_url = None

    return None

