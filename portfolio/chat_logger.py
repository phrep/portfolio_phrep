import logging
import sys

from .models import ChatLog

logger = logging.getLogger("chatbot")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)


def log_conversation(message, reply=None, error=None):
    if error:
        logger.warning("chat_error message=%r error=%s", message, error)
    else:
        logger.info("chat_ok message=%r reply=%r", message, reply)

    try:
        ChatLog.objects.create(message=message, reply=reply, error=error)
    except Exception:
        logger.exception("Falha ao gravar log de conversa no banco de dados.")
