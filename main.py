import requests
import os
import argparse

if __name__ == "__main__":
    first_message = None
    clients = [
        {
            'client': {'number': None, 'url': None}
        },

        {
            'client': {'number': None, 'url': None}
        }
    ]
    phone_number = None # Deve utilizar a biblioteca random

    client_target = None

    for client in clients:
        for a, b in client.items():
            if b['number'] == phone_number:
                client_target = b['url']

    # Pra baixo deve conter a requisição apontando para o client
    # a rota é: /envia_mensagem_para_servidor

    body = {
        "message_from": None,
        "message_to": phone_number,
        "message": first_message,
        "url_client": client_target
    }