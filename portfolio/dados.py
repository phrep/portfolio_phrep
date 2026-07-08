
Linguagens = {
    'python': {'nome': 'Python'},
    'sql': {'nome': 'SQL'},
    'pyspark': {'nome': 'PySpark'},
    'cpp_lua': {'nome': 'C++/Lua'},
}


habilidades = {
    'engenharia_dados': {
        'categoria': 'Engenharia de Dados',
        'itens': [
            'Pipelines ETL/ELT', 'Apache Airflow', 'Data Lakehouse',
            'Modelagem (Star/Snowflake Schema)', 'Particionamento de Dados', 'Integração de APIs'
        ],
    },
    'banco_dados': {
        'categoria': 'Banco de Dados',
        'itens': [
            'SQL', 'PostgreSQL', 'MySQL', 'MongoDB', 'VectorDB', 'Qdrant'
        ],
    },
    'backend_frameworks': {
        'categoria': 'Back-end & Frameworks',
        'itens': [
            'Django', 'FastAPI', 'Criação de APIs REST',
            'Django ORM', 'SQLAlchemy', 'Pydantic'
        ],
    },
    'ai_ml': {
        'categoria': 'AI & Machine Learning',
        'itens': [
            'Scikit-learn', 'Apache Spark', 'LLMs', 'LangChain',
            'RAG', 'Prompt Engineering', 'IA Generativa'
        ],
    },
    'cloud_infra': {
        'categoria': 'Cloud & Infraestrutura',
        'itens': [
            'AWS (S3, ECS, ECR, EC2, Athena, Glue, Bedrock)', 'Azure',
            'Docker', 'Terraform', 'CI/CD', 'GitHub Actions'
        ],
    },
    'bi_analytics': {
        'categoria': 'BI & Analytics',
        'itens': [
            'Python', 'Power BI', 'Power Query', 'Excel Avançado'
        ],
    },
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
},

'projeto3': {
    'titulo': 'Segmentação de Clientes por Uso de Cartão de Crédito',
    'descricao': 'Análise de aproximadamente 9.000 titulares de cartão de crédito, examinando 18 características comportamentais para segmentá-los em grupos com perfis similares e gerar insights para estratégias de marketing direcionadas.',
    'tecnologias': ['Python', 'Machine Learning', 'Jupyter Notebook', 'Scikit-learn'],
    'link_github': 'https://github.com/phrep/SEGMENTA-O_DE_CLIENTES_BASEADO_NO_USO_DO_CART-O_DE_CR-DITO'
},

'projeto4': {
    'titulo': 'Predição de Preço de Carros — Tabela FIPE',
    'descricao': 'Modelo de machine learning para prever preços de automóveis com base na tabela FIPE, incluindo análise exploratória, limpeza de dados e pipeline completo de modelagem e seleção de modelos.',
    'tecnologias': ['Python', 'Machine Learning', 'Scikit-learn', 'Jupyter Notebook'],
    'link_github': 'https://github.com/phrep/Predi-o_de_pre-o_de_carros_tabela_FIPE_Machine_learning'
},

'projeto5': {
    'titulo': 'Pipeline ETL na AWS com Terraform',
    'descricao': 'Pipeline de processamento de dados automatizada na AWS: armazena arquivos CSV no S3, cataloga com Glue Crawler, executa um Glue Job em PySpark para transformação e salva os resultados em outro bucket S3, com infraestrutura como código via Terraform.',
    'tecnologias': ['Terraform', 'Python', 'PySpark', 'AWS S3', 'AWS Glue', 'Athena'],
    'link_github': 'https://github.com/phrep/Terraform_Pipeline_ETL_AWS'
},

'projeto6': {
    'titulo': 'Portfólio Pessoal com Chatbot de IA e Observabilidade em Produção',
    'descricao': 'Desenvolvimento deste próprio portfólio em Django, com assistente virtual integrado a LLM (Groq/Llama 3.3) para responder perguntas sobre experiência e projetos. Persistência do histórico de conversas em PostgreSQL (Supabase) via Django ORM, com painel administrativo para observabilidade. Containerização com Docker, deploy contínuo via Git no Render e hardening de segurança (HSTS, rate limiting, proteção contra força bruta), tudo em infraestrutura 100% gratuita.',
    'tecnologias': ['Python', 'Django', 'PostgreSQL', 'Docker', 'LLM/Groq'],
    'link_github': 'https://github.com/phrep/portfolio_phrep'
}
}

projetos_industriais = {
    'industrial1': {
        'titulo': 'Evolução de Pipeline de dados SAP em Sistema de Gestão Industrial',
        'descricao': 'Evolução de pipeline de dados, definição squema DataWarehouse, persistencia de dados, particionamento de dados oriundos do SAP em ambiente AWS, software de gestão de chão de fábrica, abrangendo módulos MES, MPS, PCP, Supply Chain e Supply Review, com suporte a decisões de planejamento produtivo, logística e operações.',
    },
    'industrial2': {
        'titulo': 'Tradução de Regras de Negócio em Algoritmos de IA',
        'descricao': 'Levantamento e tradução de regras de negócio e processos industriais para desenvolvimento de algoritmos e incorporação em sistemas e modelos de IA.',
    },
    'industrial3': {
        'titulo': 'Rollout SAP S/4HANA · MDM',
        'descricao': 'Participação em projetos de rollout SAP S/4HANA, como Key-user de MDM (Master Data Management), desenvolvimento de automação RPA cadastros em massa e Rede neural similaridade entre cadastros.',
    },
    'industrial4': {
        'titulo': 'Governança de Dados Mestres SAP · Data Cleansing',
        'descricao': 'Estruturação, governança e limpeza data cleansing do banco de dados SAP MDM de dados mestres SAP, garantindo padronização, confiabilidade e integridade das informações para as áreas de negócio.',
    },
    'industrial5': {
        'titulo': 'Desenvolvimento de algoritmo cálculo de MRP automatico',
        'descricao': 'Algoritmo em python para cálculo ótimo de parâmetros do MRP (Material Requirements Planning) automatizado e dinâmico, baseado no consumo e lead-time de reposição. Visando otimizar o planejamento de materiais e recursos na produção.',
    },
        'industrial6': {
        'titulo': 'Desenvolvimento de Dashboard em Power BI para monitoramento de KPIs',
        'descricao': 'Desenvolvimento de dashboards interativos em Power BI para monitoramento de KPIs (Key Performance Indicators) e métricas de desempenho.',
    },
        'industrial7': {
        'titulo': 'Análise descritiva, exploratória e preditiva de dados industriais',
        'descricao': 'Desenvolvimento de análises descritivas, exploratórias e preditivas de dados industriais e de machine learning para identificar padrões, tendências e insights relevantes para a tomada de decisão.',
    },
    'industrial8': {
        'titulo': 'Portfólio Pessoal com Chatbot de IA e Observabilidade em Produção',
        'descricao': 'Desenvolvimento deste próprio portfólio em Django, com assistente virtual integrado a LLM (Groq/Llama 3.3) para responder perguntas sobre experiência e projetos. Persistência do histórico de conversas em PostgreSQL (Supabase) via Django ORM, com painel administrativo para observabilidade. Containerização com Docker, deploy contínuo via Git no Render e hardening de segurança (HSTS, rate limiting, proteção contra força bruta), tudo em infraestrutura 100% gratuita.',
    },
}