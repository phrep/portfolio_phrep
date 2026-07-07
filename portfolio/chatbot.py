import os

import requests

from .cv_context import CV_CONTEXT

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")

MAX_HISTORY_MESSAGES = 8
MAX_MESSAGE_LENGTH = 1000

SYSTEM_PROMPT = f"""Você é o assistente virtual do site portfólio de Paulo Henrique de Almeida, Engenheiro de Dados.
Responda em português, de forma breve e profissional, apenas com base nas informações do currículo abaixo.
Se a pergunta não puder ser respondida com essas informações, diga que não possui esse dado e sugira contato direto
pelo e-mail ou LinkedIn informados. Não invente experiências, datas ou habilidades que não estejam listadas.

{CV_CONTEXT}
""".strip()


class ChatbotError(Exception):
    pass


def ask_chatbot(message, history=None):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ChatbotError("Chatbot indisponível no momento.")

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for item in (history or [])[-MAX_HISTORY_MESSAGES:]:
        role = item.get("role")
        content = item.get("content")
        if role in ("user", "assistant") and isinstance(content, str):
            messages.append({"role": role, "content": content[:MAX_MESSAGE_LENGTH]})
    messages.append({"role": "user", "content": message[:MAX_MESSAGE_LENGTH]})

    try:
        response = requests.post(
            GROQ_API_URL,
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": GROQ_MODEL,
                "messages": messages,
                "temperature": 0.4,
                "max_tokens": 500,
            },
            timeout=20,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise ChatbotError("Falha ao conectar com o serviço de IA.") from exc

    data = response.json()
    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError) as exc:
        raise ChatbotError("Resposta inválida do serviço de IA.") from exc
