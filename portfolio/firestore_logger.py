import logging

from google.cloud import firestore

logger = logging.getLogger(__name__)

_db = None


def _get_client():
    global _db
    if _db is None:
        try:
            _db = firestore.Client()
        except Exception:
            logger.warning("Firestore indisponível — logging de conversas desativado.", exc_info=True)
            _db = False
    return _db or None


def log_conversation(message, reply=None, error=None):
    client = _get_client()
    if not client:
        return

    try:
        client.collection("chatbot_logs").add({
            "message": message,
            "reply": reply,
            "error": error,
            "created_at": firestore.SERVER_TIMESTAMP,
        })
    except Exception:
        logger.warning("Falha ao gravar log no Firestore.", exc_info=True)
