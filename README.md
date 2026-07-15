# Portfólio — Paulo Henrique de Almeida

Site de portfólio pessoal desenvolvido em Django, com um assistente virtual (chatbot com IA) que responde perguntas sobre experiência profissional, formação e projetos com base no meu currículo.

🔗 **Site no ar:** https://portfolio-pauloalmeida.is-a.dev

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
| Banco de dados (produção) | [Supabase](https://supabase.com/) (PostgreSQL gerenciado, free tier) |
| Containerização | Docker |
| Hospedagem | [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/) — VM Compute (Always Free tier) |
| Proxy reverso / TLS | Nginx + Let's Encrypt ([Certbot](https://certbot.eff.org/), renovação automática) |
| CI/CD | [GitHub Actions](https://github.com/features/actions) — testes, build da imagem Docker e deploy automático via SSH a cada merge na `main` |
| Controle de versão | Git / GitHub |

O conteúdo do portfólio (projetos, habilidades, formação) é servido a partir de um dicionário Python (`portfolio/dados.py`), já que é conteúdo estático que não muda por interação de usuários — não precisa de banco pra isso. O banco de dados (Postgres no Supabase) é usado para o que **é** dinâmico: o histórico de conversas do chatbot (model `ChatLog`) e os apps internos do Django (`auth`, `sessions`, `admin`).

Em desenvolvimento local, sem configurar a variável `DATABASE_URL`, o projeto cai automaticamente no SQLite (`db.sqlite3`) — assim dá pra codar e testar sem depender de internet ou arriscar gravar dados de teste no banco de produção.

---

## Funcionalidades

- **Landing page** com seções de apresentação, stack técnica, formação, projetos industriais de destaque e experiência profissional.
- **Listagem e detalhe de projetos** (`/lista_projetos/`, `/projeto/<id>/`).
- **Chatbot com IA** (canto inferior da tela): responde perguntas em português com base no currículo (`portfolio/cv_context.py`), usando a API da Groq via LLM (Llama 3.3 70B).
- **Proteção contra prompt injection** (`portfolio/chatbot.py`): system prompt com regras de segurança explícitas, heurística que bloqueia tentativas comuns de jailbreak/extração de instruções antes de chamar a API (economizando custo), e verificação pós-resposta contra vazamento do prompt de sistema. Calibrado com tentativas reais de ataque observadas em produção.
- **Rate limiting** no endpoint do chat (`portfolio/views.py`): máximo de 8 mensagens por IP a cada 60 segundos, mais um teto diário de 60 mensagens por IP — usando o cache em memória do Django, proteção contra abuso e contenção de custo da API.
- **Observabilidade do chat**: cada conversa (pergunta, resposta ou erro) é registrada em dois lugares — via `logging` padrão do Python (visível ao vivo nos Logs do Render) e persistida no Postgres (model `ChatLog`), pra consulta posterior.
- **Painel administrativo** (`/admin`): interface pronta do Django (gerada automaticamente a partir do model registrado em `portfolio/admin.py`) para visualizar, buscar e filtrar o histórico de conversas do chatbot sem precisar rodar SQL manualmente.

---

## Arquitetura

```
Navegador
   │
   ▼ HTTPS (443)
Nginx (VM Oracle) ── termina TLS (Let's Encrypt), proxy reverso
   │
   ▼ HTTP, só localhost:8080
Gunicorn (dentro do container Docker)
   │
   ├── GET /                    → view Django renderiza home.html (dados de portfolio/dados.py)
   ├── GET /lista_projetos/     → lista de projetos
   ├── GET /projeto/<id>/       → detalhe de um projeto
   │
   ├── POST /api/chat/          → chat_api (JSON)
   │       │
   │       ├── rate limit por IP + limite diário (cache do Django)
   │       ├── looks_like_injection() → bloqueia jailbreaks óbvios antes da API
   │       ├── ask_chatbot() → chama a API da Groq (LLM externo)
   │       └── log_conversation() → stdout + Postgres (model ChatLog, com IP de origem)
   │
   └── GET /admin/               → painel Django (visualizar ChatLog, gerenciar usuários)
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
  chat_logger.py         # log das conversas (stdout + banco)
  models.py               # model ChatLog (histórico de conversas)
  admin.py                 # registro do ChatLog no painel /admin
  migrations/              # migrations do Django (schema do Postgres)
  cv_context.py           # currículo em texto, usado como contexto do chatbot
  dados.py                # conteúdo do portfólio (projetos, habilidades, formação)
  templates/              # home.html, projetos.html, detalhes_projeto.html, base.html
Dockerfile              # imagem de produção (roda migrate + collectstatic + gunicorn)
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
| `ALLOWED_HOSTS` | Domínios permitidos, separados por vírgula (ex: `portfolio-pauloalmeida.is-a.dev`). |
| `CSRF_TRUSTED_ORIGINS` | Origens confiáveis para CSRF em produção (ex: `https://portfolio-pauloalmeida.is-a.dev`). |
| `SECURE_SSL_REDIRECT` | `True` força redirect HTTPS e cookies seguros (padrão). Use `False` apenas em deploys temporários sem certificado TLS configurado ainda. |
| `GROQ_API_KEY` | Chave de API da [Groq](https://console.groq.com/) para o chatbot funcionar. |
| `GROQ_MODEL` | Modelo usado no chat (padrão: `llama-3.3-70b-versatile`). |
| `DATABASE_URL` | Connection string do Postgres (Supabase) para produção. Se não definida, usa SQLite local automaticamente. |

Pra acessar o painel `/admin` em produção, crie um superusuário apontando para o banco do Supabase:
```bash
DATABASE_URL=<sua-connection-string> python manage.py createsuperuser
```

---

## Deploy

A aplicação roda numa VM Compute da **Oracle Cloud Infrastructure** (Always Free tier — sem custo), provisionada manualmente e com deploy contínuo automatizado:

1. **Infraestrutura**: VM Ubuntu 22.04 (shape `VM.Standard.E2.1.Micro`), com Security List + `iptables` liberando apenas as portas necessárias (22/SSH, 80/443).
2. **Aplicação containerizada**: a imagem é buildada a partir do `Dockerfile` (instala dependências, roda `collectstatic`, expõe o Gunicorn), e o container escuta apenas em `127.0.0.1:8080` — não é exposto direto à internet.
3. **Nginx** roda na própria VM (fora do container) como proxy reverso, recebendo tráfego público nas portas 80/443 e repassando para o Gunicorn localmente.
4. **HTTPS**: certificado TLS emitido via **Let's Encrypt** (Certbot), com renovação automática agendada.
5. **Banco de dados**: o container roda `python manage.py migrate` contra o Postgres do Supabase antes de subir o `gunicorn`, direto no `CMD` do Dockerfile.
6. **CI/CD** (`.github/workflows/ci.yml`, GitHub Actions): a cada push/PR, roda testes automatizados e valida o build da imagem Docker; a cada merge na `main`, um job de deploy conecta via SSH na VM, atualiza o código (`git pull`), rebuilda a imagem e substitui o container em produção — sem intervenção manual.
7. **Domínio**: `portfolio-pauloalmeida.is-a.dev`, registrado gratuitamente via [is-a.dev](https://is-a.dev).

---

## O que este projeto exercitou

- Backend com Django (views, templates, roteamento, arquivos estáticos).
- Consumo de API externa de LLM (Groq) e prompt engineering para restringir o assistente ao contexto do currículo.
- Modelagem de dados com Django ORM e migrations, persistindo em PostgreSQL gerenciado (Supabase).
- Uso do Django Admin para expor dados da aplicação sem construir uma interface manual.
- Proteção de endpoint: rate limiting por IP (por minuto e diário) e defesas contra prompt injection/jailbreak em um chatbot com LLM (heurística pré-chamada, hardening do system prompt, verificação de vazamento pós-resposta).
- Containerização com Docker e deploy em nuvem via Git, com banco de dados externo à plataforma de hospedagem.
- Gestão de configuração por variáveis de ambiente, com fallback entre ambientes (SQLite local / Postgres em produção) sem duplicar código.
- Provisionamento de infraestrutura cloud (Oracle Cloud Always Free): VM, VCN/subnets, security lists, firewall (`iptables`).
- Configuração de proxy reverso (Nginx) e HTTPS com certificado gratuito (Let's Encrypt/Certbot), incluindo renovação automática.
- Pipeline de CI/CD (GitHub Actions) com deploy contínuo automatizado via SSH, incluindo branch protection e revisão via Pull Request.
