from typing import Union
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
import random
import requests
import httpx

app = FastAPI()
load_dotenv()
evolution_key = os.getenv("API_KEY")
url_server = os.getenv("URL_SERVER")
instance = os.getenv("INSTANCE")

@app.post("/recebe_mensagem_servidor")
async def recebe_e_responde_mensagem (request: Request):
    '''
    Será necessário buscar o índice da mensagem
    no arquivo .env e enviar a resposta dessa mensagem
    baseado em seu índice

    Essa função deve chamar o endpoint de enviar mensagem da Evolution API
    essa função recebe uma mensagem do servidor e deve enviar uma resposta
    para o cliente que enviou a mensagem, utilizando o endpoint
    /envia_mensagem (endpoint server.py) e deve enviar também nessa função
    a mensagem utilizando o endpoint de send message da Evolution API
    '''


    re = await request.json()
    endpoint_send_message = f"http://100.0.0.31:8080/message/sendText/{instance}"
    headers = {'apikey': evolution_key}
    answer = None # Aqui você deve implementar a lógica para buscar a resposta correta
    body = {
        'number': re['message_from'],
        'textMessage': answer # será necessário buscar a resposta correta no arquivo .env
    }

    json_servidor = {
        "message_from": re['message_to'],
        "message_to": re['message_from'],
        "message": answer,
        "url_client_origem": re['url_client'],
        "url_client": re['url_client_origem']
    }
    
    send_message = requests.post(endpoint_send_message, headers=headers, json=body)
    if send_message.status_code == 200:
        print('Mensagem enviada com sucesso!')
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f'{url_server}/envia_mensagem',
                json=json_servidor,
                timeout=10.0
            )

            return response.json()
    else:
        print(f'Erro ao enviar mensagem: {send_message.status_code}')
    

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
    endpoint_send_message = f"http://100.0.0.31:8080/message/sendText/{instance}"
    
    headers = {'apikey': evolution_key}
    body = {
        'number': re['message_to'],
        'textMessage': re['message']
    }
    
    send_message = requests.post(endpoint_send_message, headers=headers, json=body)
    if send_message.status_code == 200:
        print('Mensagem enviada com sucesso!')

        async with httpx.AsyncClient() as client:
            
            response = await client.post(
                f'{url_server}/envia_mensagem',
                json=re,
                timeout=10.0
            )   
        return response.json()


