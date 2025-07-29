import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Sua URL ngrok (a mesma que você copiou)
# Certifique-se de que ela está ativa no seu terminal ngrok
NGROK_URL = "https://c5db552f2e4e.ngrok-free.app" # <-- SUA NOVA URL NGROK AQUI!
WEBHOOK_URL = f"{NGROK_URL}/webhook"

# Seu TELEGRAM_BOT_TOKEN do .env
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TELEGRAM_BOT_TOKEN:
    print("Erro: TELEGRAM_BOT_TOKEN não encontrado no seu arquivo .env")
    print("Por favor, adicione TELEGRAM_BOT_TOKEN=SEU_TOKEN_AQUI no .env e tente novamente.")
else:
    # URL da API do Telegram para configurar o webhook
    telegram_api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook"

    # Parâmetros para a requisição
    params = {
        "url": WEBHOOK_URL
    }

    print(f"Tentando configurar o webhook do Telegram para: {WEBHOOK_URL}")

    try:
        response = requests.post(telegram_api_url, params=params)
        response.raise_for_status() # Lança um erro para status HTTP 4xx/5xx

        result = response.json()
        if result.get("ok"):
            print("Webhook do Telegram configurado com sucesso!")
            print("Resultado da API:", result)
        else:
            print("Erro ao configurar o webhook do Telegram.")
            print("Resposta da API:", result)

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ou requisição: {e}")
        if response is not None:
            print(f"Resposta da API (se disponível): {response.text}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")