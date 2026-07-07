import json

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .chatbot import ChatbotError, ask_chatbot
from .dados import habilidades, projetos, Linguagens, projetos_industriais
from .chat_logger import log_conversation
from .utils import get_client_ip

CHAT_RATE_LIMIT = 8
CHAT_RATE_WINDOW = 60  # segundos


def _is_rate_limited(request):
    key = f'chat_rate:{get_client_ip(request)}'
    if cache.add(key, 1, timeout=CHAT_RATE_WINDOW):
        count = 1
    else:
        count = cache.incr(key)
    return count > CHAT_RATE_LIMIT


# Create your views here.
def home(request):
    return render(request, 'home.html', {
        'habilidades': habilidades,
        'projetos': projetos,
        'Linguagens': Linguagens,
        'projetos_industriais': projetos_industriais,
    })

def lista_projetos(request):
    return render(request, 'projetos.html',{'projetos': projetos})

def detalhes_projeto(request, id_projeto):
    projeto = projetos.get(id_projeto)
    return render(request, 'detalhes_projeto.html', {'projeto': projeto})


@require_POST
def chat_api(request):
    if _is_rate_limited(request):
        return JsonResponse(
            {'error': 'Muitas mensagens em pouco tempo. Aguarde um instante e tente novamente.'},
            status=429,
        )

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido.'}, status=400)

    message = (data.get('message') or '').strip()
    history = data.get('history') or []

    if not message:
        return JsonResponse({'error': 'Mensagem vazia.'}, status=400)
    if len(message) > 1000:
        return JsonResponse({'error': 'Mensagem muito longa.'}, status=400)
    if not isinstance(history, list):
        history = []

    try:
        reply = ask_chatbot(message, history)
    except ChatbotError as exc:
        log_conversation(message, error=str(exc))
        return JsonResponse({'error': str(exc)}, status=502)

    log_conversation(message, reply=reply)
    return JsonResponse({'reply': reply})


