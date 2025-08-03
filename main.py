import requests
import os
import argparse

if __name__ == "__main__":
    first_message = None
    phone_number = None # Deve utilizar a biblioteca random

    # Pra baixo deve conter a requisição apontando para o client
    # a rota é: /envia_mensagem_para_servidor

    body = {
        "message_from": None,
        "message_to": phone_number,
        "message": first_message,
        "url_client": None
    }