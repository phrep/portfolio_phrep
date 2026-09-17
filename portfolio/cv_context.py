from .dados import habilidades, projetos, projetos_industriais, experiencias


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


def _formatar_experiencias():
    blocos = []
    for exp in experiencias.values():
        linhas = [f"### {exp['cargo']} — {exp['empresa']} ({exp['periodo']})"]
        if exp.get('itens'):
            linhas.extend(f"- {item}" for item in exp['itens'])
        elif exp.get('texto'):
            linhas.append(exp['texto'])
        blocos.append("\n".join(linhas))
    return "\n\n".join(blocos)


CV_CONTEXT = f"""
## Sobre
Paulo Henrique de Almeida, 37 anos, nascido em 1989, em Sao jose dos campos, onde mora atualmente,  é Engenheiro com mais de 10 anos de experiência em Engenharia, Análise e Governança de
Dados, atuando em projetos industriais de grande porte envolvendo IA, SAP S/4HANA, Indústria 4.0, pipelines ETL/ELT em
ambiente cloud, migração e saneamento de dados, modelagem para analytics e automação de processos. Já atuou em
multinacionais como BRF, Heineken, Somos Educação, Valgroup, e DataBot (startup de software industrial com IA na Hypera pharma).

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

{_formatar_experiencias()}

## Projetos Pessoais
{_formatar_projetos()}

## Projetos de Destaque
{_formatar_projetos_industriais()}

## Contato
- Email: ph.89.py@gmail.com
- LinkedIn: https://www.linkedin.com/in/paulo-henrique-de-almeida-a6b6358a/
- GitHub: https://github.com/phrep
- Telefone: (12) 98815-7064
""".strip()
