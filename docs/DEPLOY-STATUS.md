# Status do deploy na Oracle Cloud

> Arquivo de acompanhamento — não faz parte do código, é só referência do que já foi feito e do que falta.

## ✅ Concluído

- **Infraestrutura**: VM `instance-20260714-1114` na Oracle Cloud (Always Free), shape `VM.Standard.E2.1.Micro` (AMD, 1 OCPU/1GB), Ubuntu 22.04, região São Paulo (`sa-saopaulo-1`).
  - IP público: `163.176.242.62`
  - VCN: `portfolio-vcn`, subnet pública `public subnet-portfolio-vcn`
  - Acesso SSH: usuário `ubuntu`, chave dedicada em `~/.ssh/oracle_portfolio`
- **Rede**: porta 80 (HTTP) liberada na Security List da Oracle **e** no `iptables` da VM (regra persistida via `iptables-persistent`). Porta 22 (SSH) liberada por padrão.
- **Aplicação**: rodando em container Docker (`docker run --name portfolio -p 80:8080 --restart unless-stopped`), a partir da imagem buildada do `Dockerfile` do projeto.
- **Banco de dados**: usa o **mesmo Postgres do Supabase** que o Render usa em produção (`DATABASE_URL` configurada no `.env` da VM, não commitado no Git).
- **Configuração de produção (`.env` da VM)**: `DEBUG=False`, `ALLOWED_HOSTS=163.176.242.62`, `SECURE_SSL_REDIRECT=False` (temporário, sem HTTPS ainda), `CSRF_TRUSTED_ORIGINS` vazio.
- **Código**: `core/settings.py` foi ajustado para desacoplar `SECURE_SSL_REDIRECT` de `DEBUG` via env var própria (default `True`, preserva comportamento do Render). Ver `.env.example` para documentação.
- **Feature**: `ChatLog` agora grava `ip_address` de quem interage com o chatbot (campo, migration, admin — PR #3 no repo do projeto).
- **CI/CD**: `.github/workflows/ci.yml` tem um job `deploy` que roda após `test` + `docker-build`, só em push direto na `main` (pós-merge de PR). Conecta via SSH (`appleboy/ssh-action`) usando os secrets do repositório `ORACLE_HOST` e `ORACLE_SSH_KEY`, e faz: `git pull` → rebuild da imagem → troca do container antigo pelo novo → `docker image prune -f`.
- **Domínio**: PR aberto em [is-a-dev/register#43696](https://github.com/is-a-dev/register/pull/43696) registrando `portfolio-pauloalmeida.is-a.dev` → A record `163.176.242.62`. **Aguardando revisão/merge dos mantenedores** (pode levar horas a dias).
- **Guia de referência local**: `docs/Guia-Deploy-Portfolio.pdf` (passo a passo genérico pra qualquer alteração futura + fluxo de PR/CI/CD).

## ✅ HTTPS configurado (concluído em 2026-07-15)

- Domínio `portfolio-pauloalmeida.is-a.dev` registrado e propagado, apontando para `163.176.242.62`.
- Porta 443 liberada na Security List da Oracle e no `iptables` da VM (persistida).
- `.env` da VM atualizado: `ALLOWED_HOSTS` inclui o domínio, `CSRF_TRUSTED_ORIGINS=https://portfolio-pauloalmeida.is-a.dev`, `SECURE_SSL_REDIRECT=True`.
- Nginx instalado na VM (fora do Docker) como proxy reverso: escuta 80/443 publicamente, repassa pra `127.0.0.1:8080` (container, que não expõe mais porta pra internet diretamente).
  - Config em `/etc/nginx/sites-available/portfolio` (symlink em `sites-enabled`).
- Certificado TLS emitido via Certbot (`sudo certbot --nginx -d portfolio-pauloalmeida.is-a.dev`) — renovação automática já agendada (systemd timer do certbot).
- Container Docker recriado com `-p 127.0.0.1:8080:8080` (só acessível localmente, não mais exposto direto na porta 80).
- `.github/workflows/ci.yml` (job `deploy`) atualizado para usar `-p 127.0.0.1:8080:8080` em vez de `-p 80:8080`, mantendo compatibilidade com o Nginx em deploys futuros.
- Testado: `https://portfolio-pauloalmeida.is-a.dev` retorna 200 OK, com HSTS e cookies `Secure` ativos.

## ⏳ Pendente / próximos passos possíveis

- Testar login em `/admin` e o chatbot via HTTPS no domínio novo (confirmação final end-to-end).
- Considerar redirecionar/desativar o acesso direto por IP (`163.176.242.62`) se não fizer mais sentido mantê-lo público, já que o domínio é o canal principal agora.
- Sem urgência: kernel da VM tem atualização pendente (`6.8.0-1057-oracle`) — aplicar num momento de manutenção (`sudo reboot`), não é crítico.

## Referências rápidas

- SSH na VM: `ssh -i ~/.ssh/oracle_portfolio ubuntu@163.176.242.62`
- Pasta do projeto na VM: `~/portfolio_phrep`
- Repo do domínio (fork local): `~/is-a-dev-register` (no PC local, não na VM)
