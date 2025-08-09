# 🔥 WhatsBurner (Maturador de Chips para WhatsApp)

O **WhatsBurner** é um sistema em **Python + FastAPI** desenvolvido para realizar o *aquecimento gradual* de números de WhatsApp, enviando mensagens de forma controlada para evitar bloqueios e banimentos.

Ideal para cenários onde é necessário preparar chips novos antes de usá-los em campanhas, mantendo um histórico de envio saudável e construindo uma reputação positiva para o número.

## 🚀 Funcionalidades

- **Aquecimento automático** de chips com envio controlado de mensagens.
- Controle de múltiplos números simultaneamente.
- Servidor em FastAPI para rotear mensagens que chegam no número

## 📂 Estrutura do Projeto

```
maturador/
│
├── main.py        # Script principal para iniciar o sistema
├── server.py      # Servidor FastAPI que expõe as rotas de integração
├── client.py      # Cliente para envio/processamento de mensagens
├── conversas.py   # Lógica de controle de conversas e tempo entre mensagens
└── .env           # Configurações sensíveis (tokens, instâncias, etc.)
```

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/pedromakaveli/WhatsBurner.git
   cd maturador
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o arquivo `.env`:
   ```env
   INSTANCE=sua_instancia_evolution
   TOKEN=seu_token_evolution
   ```

## ▶️ Execução

Cada máquina deve ter o arquivo client.py e main.py, cada máquina é representada por um client que envia pacotes Json para o servidor.
O arquivo main.py realiza o disparo da primeira mensagem apontando para o seu client.py localizado na máquina.

Exemplo de fluxo: A => B => A
B => C => B

Ou seja: Temos 3 números (A, B, C), A envia mensagens para B que responde e devolve a mensagem para A
enquanto isso no arquivo main.py de B, ele envia mensagens para C que também responde B

Para rodar o servidor:
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

Para rodar o cliente:
```bash
python client.py
```

Para começar a maturar
```bash
python main.py
```

## 📌 Fluxo de Funcionamento

1. Inicialização arquivo main.py
2. Recebiment do Json no client local da máquina
3. Servidor recebe o Json vindo dos clients e encaminha para o client destino
4. Cliente destino responde e reenvia o Json para o servidor, dessa vez fazendo o caminho reverso (De volta ao client origem)

## 🛠 Tecnologias

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **Requests**
- **Dotenv**

## ⚠️ Aviso Legal

Este projeto tem finalidade educacional e de pesquisa.  
O uso indevido para envio massivo ou spam pode resultar em bloqueios permanentes.  
Respeite as políticas e leis aplicáveis.