import logging
import sys

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
