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
    
    async with httpx.AsyncClient() as client:
        try:
            # Envia para o CLIENT na porta 8080
            response = await client.post(
                'http://127.0.0.1:8080/recebe_mensagem_servidor',
                json={'mensagem_real': body},
                timeout=10.0
            )
            return response.json()
        except httpx.RequestError as e:
            return {"error": f"Falha na comunicação: {str(e)}"}