
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
    'titulo': 'Pipeline ETL Distribuído com Airflow',
    'descricao': 'Desenvolvimento de um pipeline ETL distribuído utilizando Airflow e Celery para processamento de dados em escala.',
    'tecnologias': ['Python', 'Airflow', 'Docker'],
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
    'industrial0': {
        'titulo': 'Digitalização de Processos Industriais, regras de Negócio em Algoritmos de IA',
        'descricao': 'Digitalização de processos industriais de alta complexidades em algoritmos e incorporação em sistema e modelos de IA Generativa, através de pipeline de dados cloud, langchain, MCP, RAG e Banco de dados vetoriais Qdrant',
    },
    'industrial1': {
        'titulo': 'Evolução de Pipeline de dados SAP em Sistema de Gestão Industrial',
        'descricao': 'Evolução de software de gestão de chão de fábrica (Databot), módulos Supply Review (MES, MPS, PCP, Supply Chain',
    },
    'industrial2': {
        'titulo': 'Desenvolvimento de algoritmo de similaridade textual (NLP) para deduplicação de cadastros em massa',
        'descricao': 'Desenvolvimento de algoritmo de similaridade textual utilizando TF-IDF e similaridade de cosseno para identificação de cadastros de materiais duplicados ou equivalentes em bases de grande volume.',
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


# Fonte única das experiências profissionais: alimenta tanto o CV_CONTEXT (IA)
# quanto a seção "Experiência Profissional" do site (home.html).
experiencias = {
    'databot': {
        'periodo': 'Jan 2026 – Abr 2026 · São José dos Campos, SP',
        'cargo': 'Analista de Dados Sênior',
        'empresa': 'DataBot Software IA S.A · Software Industrial',
        'itens': [
            'Evolução de software de gestão de chão de fábrica, módulo Supply Review (MES, MPS, PCP, Supply Chain) com foco em planejamento e controle da produtivo;',
            'Digitalização de processos industriais de alta complexidades em algoritmos e incorporação em sistema e modelos de IA Generativa, através de pipeline de dados cloud, langchain, LLM, MCP, RAG e Banco de dados vetoriais Qdrant;',
            'Condução de reuniões com áreas de negócio (PCP, planejamento produtivo, logística e supply chain), traduzindo regras operacionais em algoritmos, modelos analíticos e lógicas de otimização;',
            'Desenvolvimento e integração de algoritmos e modelos utilizando Python, C++ e Lua, aplicados à tomada de decisão em ambientes industriais;',
            'Aplicação de análise de dados voltada ao contexto produtivo, suportando decisões relacionadas a capacidade, demanda, planejamento e eficiência operacional;',
            'Atuação no suporte técnico e análise de incidentes, garantindo estabilidade e evolução contínua de pipelines e sistemas críticos;',
        ],
    },
    'valgroup': {
        'periodo': 'Fev 2025 – Nov 2025 · Lorena, SP',
        'cargo': 'Analista de Dados Mestres',
        'empresa': 'Valgroup · Indústria de Embalagens',
        'itens': [
            'Estudos estatísticos avançados, análises descritiva, exploratória e preditivas.',
            'Desenvolvimento de RPA, aplicações e automações para otimizar fluxos de cadastro e manutenção de dados mestres com utilização de tecnologia (Python / SAP Script / IA / LLM / Web scraping).',
            'Desenvolvimento de algoritmo de similaridade textual utilizando TF-IDF e similaridade de cosseno para identificação de cadastros de materiais duplicados ou equivalentes em bases de grande volume.',
            'Evolução de pipeline de dados, desenvolvimento e manutenção de dashoboards em Power BI.',
            'Governança de dados e banco de dados de várias fontes: Excel, Google BigQuery, SQL;',
            'Atuação como Key User em projetos de implantação SAP S/4HANA, suportando definição, padronização, classificação e implementação de processos de Dados Mestres de Materiais, baseado em análise de banco de dados de cadastro de materiais industriais SAP.',
            'Validação de processos, criação de documentação e treinamento de usuários durante e após o go-live.',
            'Classificação, padronização e saneamento dos materiais, definição e implementação de PDM (padrão descritivo), validação técnica, eliminação de duplicidades, organização de famílias, estruturação de grupos e tipos de materiais. Alteração de status de materiais, obsolescência e bloqueios de códigos SAP.',
            'Suporte contínuo às áreas de Compras, Engenharia, Logística, PCM e Produção, garantindo padronização e confiabilidade dos dados mestres no SAP.',
            'Gestão de solicitações de cadastro de materiais e serviços em software PIPEFY metodologia KANBAN, assegurando integridade, padronização às regras da governança de dados mestres.',
        ],
    },
    'heineken': {
        'periodo': 'Out 2021 – Ago 2024',
        'cargo': 'Analista Corporativo de Inteligência de Manutenção',
        'empresa': 'Heineken · Indústria de Bebidas',
        'itens': [
            'Suporte em análise e inteligência de dados para manutenção e planejamento MRP nas 12 principais fábricas do Brasil;',
            'Governança com PCM e procurement: apresentação de análises descritivas, exploratórias, resultados de indicadores e Dashboards. Gerando insights e criando planos de ação junto a áreas de negócio metodologia Waterfall;',
            'Gestão de cadastro de materiais, controle de estoque, parametrização e análises para otimização de níveis de estoque;',
            'Desenvolvimento de dashboards Power BI e automações em Python;',
            'Projeto Algoritmo MRP: Projeto desenvolvido em programa interno na Heineken, Data Super Stars. Pipeline de dados e algoritmo de machine learning e Python que calcula os parâmetros ideais de acordo com o histórico de consumo dos materiais e regras de negócio, provendo automatização de gestão e conceito de parâmetros de estoque dinâmicos;',
            'Projeto Contratos locais: Business case de fornecedores locais, análise de dados estratégicos, classificação de materiais críticos e fornecedores locais com baixo lead time por planta/regional. Desenvolvimento de contratos com fornecedores locais, visando automação de pedidos e diminuição de lead time total no fluxo de reposição automático MRP;',
            'Projeto Data cleasing: Classificação, organização, Análise de similaridade de cadastros, Limpeza e unificação de códigos SAP de materiais;',
        ],
    },
    'inicial': {
        'periodo': '2011 – 2018',
        'cargo': 'Trajetória inicial em Operações e Compras',
        'empresa': 'BRF (Sadia/Perdigão) · Somos Educação · IPPLAN',
        'texto': 'Base sólida em logística, suprimentos e melhoria contínua: gestão de manutenção e frota, indicadores de desempenho, roteirização, cotações, negociações e gestão de contratos.',
    },
}