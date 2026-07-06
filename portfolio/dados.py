from os import link


habilidades = {
'habilidade1': {
    'nome': 'Python',
},
'habilidade2': {
    'nome': 'SQL',
},
'habilidade3': {
    'nome': 'DJANGO',
}
}

projetos = {
'projeto1': {
    'titulo': 'Text-to-SQL com RAG AWS',
    'descricao': 'Conversão de linguagem natural em consultas SQL com LLMs + recuperação de contexto (RAG), executando queries e gerando insights automaticamente.',
    'tecnologias': ['Python', 'SQL', 'AWS', 'LangChain', 'LlamaIndex'],
    'link_github': 'https://github.com/phrep/LLM_TEXT-TO-SQL_AWS_PRF'
},


'projeto2': {
    'titulo': 'Pipeline ETL Distribuído com Airflow e Celery',
    'descricao': 'Desenvolvimento de um pipeline ETL distribuído utilizando Airflow e Celery para processamento de dados em escala.',
    'tecnologias': ['Python', 'Airflow', 'Celery', 'Docker'],
    'link_github': 'https://github.com/phrep/Pipeline_ETL_Airflow_API_Schiphol'
}
}