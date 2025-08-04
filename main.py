import requests
import os
import argparse
from dotenv import load_dotenv

if __name__ == "__main__":
    first_message = None
    my_phone_number = "Seu número de telefone"
    phone_number = "Número de telefone destinatário"
    my_client = "http://100.0.0.69:8080"
    client_target = "http://100.0.0.69:8000"

    # Pra baixo deve conter a requisição apontando para o client
    # a rota é: /envia_mensagem_para_servidor

    load_dotenv()
    body = {
        "instance": os.getenv("INSTANCE"),
        "message_from": my_phone_number,
        "message_to": phone_number,
        "message": first_message,
        "url_client_origem": my_client,
        "url_client": client_target
    }
    
    re = requests.post(f"{my_client}/envia_mensagem_para_servidor", json=body)
    
    print(re.json())