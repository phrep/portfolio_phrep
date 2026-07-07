from .dados import habilidades, projetos, projetos_industriais


def _formatar_habilidades():
    linhas = [f"- {dados['categoria']}: {', '.join(dados['itens'])}" for dados in habilidades.values()]
    return "\n".join(linhas)


def _formatar_projetos():
    linhas = [
        f"- {p['titulo']}: {p['descricao']} (Tecnologias: {', '.join(p['tecnologias'])}) — {p['link_github']}"
        for p in projetos.values()
    ]
    return "\n".join(linhas)


def _formatar_projetos_industriais():
    linhas = [f"- {p['titulo']}: {p['descricao']}" for p in projetos_industriais.values()]
    return "\n".join(linhas)


CV_CONTEXT = f"""
## Sobre
Paulo Henrique de Almeida, 37 anos, nascido em 1989, em Sao jose dos campos, onde mora atualmente,  é Engenheiro com mais de 10 anos de experiência em Engenharia, Análise e Governança de
Dados, atuando em projetos industriais de grande porte envolvendo IA, SAP S/4HANA, Indústria 4.0, pipelines ETL/ELT em
ambiente cloud, migração e saneamento de dados, modelagem para analytics e automação de processos. Já atuou em
multinacionais como BRF, Heineken, Somos Educação e Valgroup, além de uma empresa de software industrial com
Inteligência Artificial.

## Formação
- Pós-graduação em IA e Ciência de Dados — Anhembi Morumbi (cursando)
- Bacharel em Engenharia Mecânica — Anhanguera, 2019
- Tecnólogo em Logística — IBTA, 2010

## Cursos e Certificações
- Redes Neurais e Processamento de Linguagem Natural - Anhembi Morumbi
- AWS Data Engineer Associate 2026 (Hands On)
- Engenheiro de Agentes de IA — Asimov Academy
- Lean 6 Sigma Green Belt — FM2S
- Data Super Stars (Machine Learning) — Heineken/Fabwork
- Machine learning - Alura
- SQL - Alura
- Python - Alura

## Idiomas
- Inglês — Intermediário/Avançado
- Espanhol — Básico

## Stack Técnica
{_formatar_habilidades()}

## Experiência Profissional

### Analista de Dados Sênior — DataBot Software IA S.A · Software Industrial (Jan 2026 – Abr 2026, São José dos Campos, SP)
- Desenvolvimento de soluções de IA utilizando Python e LangChain, aplicadas à automação de análises e geração de
  insights para operações industriais.
- Atuação no sistema de gestão de chão de fábrica (Databot), módulos MPS, MES, PCP, Supply Chain e Supply Review.
- Desenvolvimento e integração de algoritmos e modelos (incluindo redes neurais) em Python, C++ e Lua.
- Construção de pipelines de dados em AWS (ETL) e modelagem em PostgreSQL e MongoDB.

### Analista de Dados Mestres — Valgroup · Indústria de Embalagens (Fev 2025 – Nov 2025, Lorena, SP)
- Key User em projeto de implantação SAP S/4HANA, governança de dados mestres de materiais.
- RPA e automações (Python, SAP Script, IA/LLM, web scraping).
- Análises de similaridade com NLP e Machine Learning, dashboards em Power BI.

### Analista Corporativo de Inteligência de Manutenção — Heineken · Indústria de Bebidas (Out 2021 – Ago 2024)
- Inteligência de dados para manutenção e planejamento MRP nas 12 principais fábricas do Brasil.
- Dashboards em Power BI e automações em Python.
- Projeto premiado Algoritmo MRP (Data Super Stars), projetos de contratos locais e data cleansing de códigos SAP.

### Trajetória inicial em Operações e Compras — BRF (Sadia/Perdigão), Somos Educação, IPPLAN (2011 – 2018)
- Gestão de manutenção e frota, indicadores de desempenho, roteirização, cotações, negociações e gestão de contratos.

## Projetos Pessoais
{_formatar_projetos()}

## Projetos Industriais de Destaque
{_formatar_projetos_industriais()}

## Contato
- Email: ph.89.py@gmail.com
- LinkedIn: https://www.linkedin.com/in/paulo-henrique-de-almeida-a6b6358a/
- GitHub: https://github.com/phrep
- Telefone: (12) 98815-7064
""".strip()
