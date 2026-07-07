# Portfólio — Paulo Henrique de Almeida

Site de portfólio pessoal desenvolvido em Django, com um assistente virtual (chatbot com IA) que responde perguntas sobre experiência profissional, formação e projetos com base no meu currículo.

🔗 **Site no ar:** https://portfolio-paulo-ph89.onrender.com

Este foi meu primeiro projeto fullstack em Python — construído para consolidar conhecimento em desenvolvimento web (Django), integração com APIs externas (LLM), containerização (Docker) e deploy em nuvem.

---

## Stack utilizada

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.11 |
| Framework web | Django 5.2 |
| Servidor WSGI (produção) | Gunicorn |
| Arquivos estáticos | WhiteNoise |
| Frontend | HTML5, CSS3, JavaScript (vanilla, sem frameworks) |
| IA / Chatbot | [Groq API](https://groq.com/) — modelo `llama-3.3-70b-versatile` |
| Containerização | Docker |
| Hospedagem | [Render](https://render.com/) (Web Service via Docker, plano free) |
| Controle de versão | Git / GitHub |

Não há banco de dados de aplicação (Postgres/MySQL) — o conteúdo do portfólio (projetos, habilidades, formação) é servido a partir de um dicionário Python (`portfolio/dados.py`), já que o conteúdo é estático e não muda por interação de usuários. O SQLite padrão do Django (`db.sqlite3`) só existe para suportar os apps internos do framework (`auth`, `sessions`, `admin`), que não são usados ativamente neste projeto.

---

## Funcionalidades

- **Landing page** com seções de apresentação, stack técnica, formação, projetos industriais de destaque e experiência profissional.
- **Listagem e detalhe de projetos** (`/lista_projetos/`, `/projeto/<id>/`).
- **Chatbot com IA** (canto inferior da tela): responde perguntas em português com base no currículo (`portfolio/cv_context.py`), usando a API da Groq via LLM (Llama 3.3 70B).
- **Rate limiting** no endpoint do chat (`portfolio/views.py`): máximo de 8 mensagens por IP a cada 60 segundos, usando o cache em memória do Django — proteção simples contra abuso do endpoint.
- **Observabilidade do chat**: cada conversa (pergunta, resposta ou erro) é registrada via `logging` padrão do Python, capturado automaticamente pelos logs do serviço no Render (sem depender de nenhum serviço externo).

---

## Arquitetura

```
Navegador
   │
   ├── GET /                    → view Django renderiza home.html (dados de portfolio/dados.py)
   ├── GET /lista_projetos/     → lista de projetos
   ├── GET /projeto/<id>/       → detalhe de um projeto
   │
   └── POST /api/chat/          → chat_api (JSON)
           │
           ├── rate limit por IP (cache do Django)
           ├── ask_chatbot() → chama a API da Groq (LLM externo)
           └── log_conversation() → stdout (visível nos Logs do Render)
```

O chatbot **não roda nenhum modelo de IA localmente** — a view apenas monta o histórico da conversa, envia para a API da Groq via HTTP (`portfolio/chatbot.py`) e repassa a resposta. Isso mantém a aplicação leve, já que todo o processamento pesado de inferência acontece do lado da Groq.

---

## Estrutura do projeto

```
core/                   # configurações do projeto Django
  settings.py           # settings lidos via variáveis de ambiente (.env)
  static/                # CSS, JS e imagens globais
portfolio/              # app principal
  views.py              # views (home, projetos, chat_api) + rate limit
  urls.py                # rotas do app
  chatbot.py             # integração com a API da Groq
  chat_logger.py         # log das conversas via stdout
  cv_context.py           # currículo em texto, usado como contexto do chatbot
  dados.py                # conteúdo do portfólio (projetos, habilidades, formação)
  templates/              # home.html, projetos.html, detalhes_projeto.html, base.html
Dockerfile              # imagem de produção (gunicorn + collectstatic)
requirements.txt        # dependências Python
.env.example            # modelo das variáveis de ambiente necessárias
```

---

## Rodando localmente

**Pré-requisitos:** Python 3.11+.

```bash
git clone https://github.com/phrep/portfolio_phrep.git
cd portfolio_phrep
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt

cp .env.example .env         # depois edite o .env com seus valores
python manage.py migrate
python manage.py runserver
```

Acesse em `http://127.0.0.1:8000`.

### Variáveis de ambiente

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django. Gere uma nova para produção (nunca reutilize a de desenvolvimento). |
| `DEBUG` | `True` em desenvolvimento, `False` em produção. |
| `ALLOWED_HOSTS` | Domínios permitidos, separados por vírgula (ex: `meusite.onrender.com`). |
| `CSRF_TRUSTED_ORIGINS` | Origens confiáveis para CSRF em produção (ex: `https://meusite.onrender.com`). |
| `GROQ_API_KEY` | Chave de API da [Groq](https://console.groq.com/) para o chatbot funcionar. |
| `GROQ_MODEL` | Modelo usado no chat (padrão: `llama-3.3-70b-versatile`). |

---

## Deploy

A aplicação é containerizada com Docker e hospedada no **Render** (Web Service, plano Free — sem custo, sem cartão de crédito exigido):

1. O Render builda a imagem a partir do `Dockerfile` na raiz do repositório.
2. `collectstatic` roda no build, servindo os arquivos estáticos via WhiteNoise.
3. `gunicorn` sobe a aplicação escutando na porta definida pela variável `PORT`.
4. Variáveis de ambiente de produção são configuradas diretamente no painel do Render (não versionadas no repositório).
5. Auto-deploy ativado: todo `git push` na branch `main` dispara um novo build automaticamente.

**Limitação do plano free:** a instância "dorme" após ~15 minutos sem tráfego; a primeira requisição depois disso pode levar 30-60s para responder (cold start).

---

## O que este projeto exercitou

- Backend com Django (views, templates, roteamento, arquivos estáticos).
- Consumo de API externa de LLM (Groq) e prompt engineering para restringir o assistente ao contexto do currículo.
- Proteção básica de endpoint (rate limiting por IP).
- Containerização com Docker e deploy em nuvem via Git.
- Gestão de configuração por variáveis de ambiente, separando segredos de código-fonte.
