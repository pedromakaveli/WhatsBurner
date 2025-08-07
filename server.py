from typing import Union
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
import random
import requests
import httpx  # Use cliente HTTP assíncrono

app = FastAPI()

@app.post('/envia_mensagem')
async def envia_mensagem(request: Request):
    body = await request.json()

    #client_url = body['payload']['url_client_origem']

    
    async with httpx.AsyncClient() as client:
        try:
            # Envia para o CLIENT na porta 8080
            response = await client.post(
                f'{body["payload"]["url_client_origem"]}/recebe_mensagem_servidor',
                json=body,
                timeout=30.0
            )
            return response.json()
        except httpx.RequestError as e:
            return {"error": f"Falha na comunicação: {str(e)}"}

    return body
