import logging
from flask import current_app
import requests
import json
import google.generativeai as genai


def process_message_from_llm(user_message):
    """
    Integra a mensagem do usuário com o modelo Gemini e retorna a resposta.
    """
    logging.info(f"Chamando Gemini com a mensagem: {user_message}")

    try:
        gemini_api_key = current_app.config.get("GEMINI_API_KEY")
        if not gemini_api_key:
            logging.error("GEMINI_API_KEY não está configurado nas variáveis de ambiente.")
            return "Desculpe, a chave da API do Gemini não está configurada."

        genai.configure(api_key=gemini_api_key)

        # A CORREÇÃO ESTÁ AQUI: Definimos o modelo e a system_instruction para idioma e papel
        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction="Você é um técnico de campo especializado em agricultura do Nordeste brasileiro e tecnologia agrícola. Seu objetivo é fornecer orientações práticas, dicas diretas e soluções eficientes para os desafios dos agricultores, de forma clara e acessível, sempre focado em resultados no campo e sustentabilidade. **Sempre responda em português.**"
        )

        # Adiciona um timeout de 60 segundos para a chamada da API
        response = model.generate_content(user_message, request_options={"timeout": 60})

        return response.text

    except Exception as e:
        logging.error(f"Erro ao chamar o modelo Gemini: {e}", exc_info=True)
        return "Desculpe, houve um erro ao processar sua solicitação com a IA. Tente novamente mais tarde."


def send_telegram_message(chat_id, text):
    """Envia uma mensagem de volta para o usuário do Telegram."""
    bot_token = current_app.config.get("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        logging.error("TELEGRAM_BOT_TOKEN não está configurado nas variáveis de ambiente.")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logging.info(f"Mensagem do Telegram enviada para {chat_id}: {text}")
        return response.json()
    except requests.exceptions.HTTPError as e:
        logging.error(f"Erro HTTP ao enviar mensagem do Telegram: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na requisição ao enviar mensagem do Telegram: {e}")


def process_telegram_message(body):
    """Processa uma mensagem de Telegram recebida."""
    try:
        message = body.get("message", {})
        chat_id = message.get("chat", {}).get("id")
        user_text = message.get("text")

        if chat_id and user_text:
            logging.info(f"Mensagem do Telegram recebida de {chat_id}: {user_text}")

            llm_response = process_message_from_llm(user_text)

            send_telegram_message(chat_id, llm_response)
        else:
            logging.warning("Estrutura de mensagem do Telegram inválida ou nenhum texto encontrado.")

    except Exception as e:
        logging.error(f"Erro em process_telegram_message: {e}", exc_info=True)


def is_valid_telegram_message(body):
    """Verifica se o corpo do webhook recebido é uma mensagem de Telegram válida."""
    return "message" in body and body["message"].get("chat", {}).get("id") is not None