import requests
import os
import argparse
from dotenv import load_dotenv
from conversas import respostas
import json

if __name__ == "__main__":
    first_message = "E aí"
    my_phone_number = "Seu número de telefone"
    phone_number = "Número de telefone destinatário"
    my_client = "http://100.0.0.69:8000"

    # Pra baixo deve conter a requisição apontando para o client
    # a rota é: /envia_mensagem_para_servidor
    
    print(respostas)

    load_dotenv()
    body = {
        "payload": {
            "instance": "bot_01",
            "message_from": "553597324953",
            "message_to": "553597575163",
            "message": first_message,
            "url_client_origem": "http://100.0.0.69:8000",
            "url_client": "http://100.0.0.71:8000",
            "conversas": respostas
        }
    }
    
    re = requests.post(f"{my_client}/envia_mensagem_para_servidor", json=body)
    
    print(re.text)