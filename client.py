from typing import Union
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
import random
import requests
import httpx
from conversas import respostas
import json

app = FastAPI()
load_dotenv()
evolution_key = os.getenv("API_KEY")
url_server = os.getenv("URL_SERVER")
instance = os.getenv("INSTANCE")

@app.post("/recebe_mensagem_servidor")
async def recebe_e_responde_mensagem(request: Request):
    
    try:
        # 1. Obter dados da requisição
        data = await request.json()
        
        payload = data.get('payload', {})
        
        # 2. Obter resposta da mensagem
        message = payload.get("message", "")
        answer = respostas.get(message, "Resposta padrão (mensagem não reconhecida)")
        print(message, answer)
        
        # 3. Preparar resposta para o cliente (simulação)
        response_payload = {
            "payload": {
                "message_from": payload.get('message_to', ''),
                "message_to": payload.get('message_from', ''),
                "message": answer,
                "url_client_origem": payload.get('url_client', ''),
                "url_client": payload.get('url_client_origem', '')
            }
        }
        endpoint_send_message = f"http://100.0.0.31:8080/message/sendText/{instance}"
        headers = {'apikey': evolution_key}
        body = {
            "number": data['payload']['message_from'],
            "textMessage": {
            "text": data['payload']['message']
            }
        }
            
        send_message = requests.post(endpoint_send_message, headers=headers, json=body)
        
        if send_message.status_code == 200:
            print('Mensagem enviada com sucesso!')
        
        # 4. Enviar resposta para o servidor
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f'{url_server}/envia_mensagem',
                json=response_payload,
                timeout=10.0
            )
        
        # 5. Retornar confirmação
        return {"status": "success", "message": answer}
        
    except Exception as e:
        return {"error": f"Erro ao processar mensagem: {str(e)}"}
    

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
        "number": re['payload']['message_to'],
        "textMessage": {
            "text": re['payload']['message']
        }
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

    




