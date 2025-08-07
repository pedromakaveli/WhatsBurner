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
    my_client = "http://127.0.0.1:8080"
    client_target = "http://100.0.0.69:8000"

    # Pra baixo deve conter a requisição apontando para o client
    # a rota é: /envia_mensagem_para_servidor

    load_dotenv()
    body = {
        "payload": {
            "instance": "minha_instancia",
            "message_from": "5511999999999",
            "message_to": "5511888888888",
            "message": first_message,
            "url_client_origem": "http://127.0.0.1:8080",
            "url_client": "http://127.0.0.1:8081"
        }
    }
    
    re = requests.post(f"{my_client}/envia_mensagem_para_servidor", json=body)
    
    print(re.text)