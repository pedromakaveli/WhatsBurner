from typing import Union
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
import random
import requests

app = FastAPI()

@app.post('/envia_mensagem')
async def envia_mensagem(request: Request):
    '''
    Endpoint para enviar uma mensagem para o cliente
    '''
    body = await request.json()
    
    # Aqui você pode implementar a lógica para enviar a mensagem
    # Por exemplo, utilizando a Evolution API ou outro serviço
    
    
    
    return {"status": "Mensagem enviada com sucesso", "data": body}