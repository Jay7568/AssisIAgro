import logging
import json

from flask import Blueprint, request, jsonify, current_app

from .decorators.security import signature_required
# Mantenha as importações do WhatsApp por enquanto, mesmo que não sejam usadas diretamente pelo Telegram
from .utils.whatsapp_utils import (
    process_whatsapp_message,
    is_valid_whatsapp_message,
)
# ADICIONE estas importações para lidar com o Telegram
from .utils.telegram_utils import process_telegram_message, is_valid_telegram_message


webhook_blueprint = Blueprint("webhook", __name__)


def handle_message():
    """
    Lida com eventos de webhook recebidos.
    Agora adaptado para processar mensagens do Telegram.
    """
    body = request.get_json()
    logging.info(f"Corpo da requisição do webhook recebida: {json.dumps(body, indent=2)}")

    try:
        # Tenta processar como uma mensagem do Telegram
        if is_valid_telegram_message(body):
            process_telegram_message(body)
            return jsonify({"status": "ok"}), 200
        # Se você eventualmente for integrar WhatsApp, pode adicionar uma condição aqui:
        # elif is_valid_whatsapp_message(body):
        #     process_whatsapp_message(body)
        #     return jsonify({"status": "ok"}), 200
        else:
            logging.warning("Evento recebido não é uma mensagem válida do Telegram ou um evento reconhecido.")
            # Se não for uma mensagem válida do Telegram, você pode querer logar ou lidar com outras plataformas
            return jsonify({"status": "error", "message": "Mensagem do Telegram não reconhecida ou inválida"}), 400

    except json.JSONDecodeError:
        logging.error("Falha ao decodificar JSON do webhook.")
        return jsonify({"status": "error", "message": "JSON inválido fornecido"}), 400
    except Exception as e:
        logging.error(f"Erro ao processar a mensagem do webhook: {e}", exc_info=True)
        return jsonify({"status": "error", "message": f"Erro interno do servidor: {e}"}), 500


# Verificação de webhook para WhatsApp (pode ser usado para verificar o Telegram também, se necessário)
def verify():
    # Analisa parâmetros da requisição de verificação do webhook
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    # Verifica se um token e modo foram enviados
    if mode and token:
        # Verifica se o modo e o token enviados estão corretos
        if mode == "subscribe" and token == current_app.config["VERIFY_TOKEN"]:
            # Responde com 200 OK e o token de desafio da requisição
            logging.info("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            # Responde com '403 Forbidden' se os tokens de verificação não corresponderem
            logging.info("VERIFICATION_FAILED")
            return jsonify({"status": "error", "message": "Verificação falhou"}), 403
    else:
        # Responde com '400 Bad Request' se os parâmetros estiverem faltando
        logging.info("MISSING_PARAMETER")
        return jsonify({"status": "error", "message": "Parâmetros faltando"}), 400


@webhook_blueprint.route("/webhook", methods=["GET"])
def webhook_get():
    return verify()

@webhook_blueprint.route("/webhook", methods=["POST"])
@signature_required
def webhook_post():
    return handle_message()