from functools import wraps
from flask import current_app, jsonify, request
import logging
import hashlib
import hmac


def validate_signature(payload, signature):
    """
    Validate the incoming payload's signature against our expected signature
    """
    # Use the App Secret to hash the payload
    expected_signature = hmac.new(
        bytes(current_app.config["APP_SECRET"], "latin-1"),
        msg=payload.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()

    # Check if the signature matches
    return hmac.compare_digest(expected_signature, signature)


def signature_required(f):
    """
    Decorator to ensure that the incoming requests to our webhook are valid and signed with the correct signature.
    Temporarily disabled for Telegram testing, as Telegram webhooks do not use this type of signature.
    For WhatsApp, this validation is crucial.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        # --- ATENÇÃO ---
        # Para que o Telegram funcione, estamos TEMPORARIAMENTE desativando a verificação de assinatura.
        # O Telegram não envia o cabeçalho 'X-Hub-Signature-256' que é esperado aqui (ele é do WhatsApp).
        # Quando você for integrar com o WhatsApp, precisará reativar e adaptar esta lógica
        # para diferenciar as requisições do WhatsApp das do Telegram.
        # Por enquanto, vamos permitir que todas as requisições cheguem ao chatbot.
        # --- FIM DA ATENÇÃO ---

        # As linhas abaixo foram comentadas/removidas para permitir que o Telegram passe.
        # signature = request.headers.get("X-Hub-Signature-256", "")[7:]
        # if not validate_signature(request.data.decode("utf-8"), signature):
        #     logging.info("Signature verification failed!")
        #     return jsonify({"status": "error", "message": "Invalid signature"}), 403

        return f(*args, **kwargs) # Permite que a função original seja executada
    return decorated_function