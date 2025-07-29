Markdown

# AssisIAgro - Assistente Agrícola para Telegram 🌾🤖

Um chatbot abrangente baseado em Flask, projetado para agricultores e comunidades agrícolas. O bot integra-se com a IA Gemini do Google para fornecer aconselhamento agrícola inteligente, identificação de doenças em culturas, informações de mercado e detalhes de programas governamentais. Construído com memória de conversação e suporte multilíngue para atender os agricultores de forma eficaz.

## Funcionalidades ✨

- **🌾 Inteligência Agrícola**: Respostas de IA especializadas para consultas agrícolas, manejo de culturas e melhores práticas
- **🔍 Detecção de Doenças em Culturas**: Análise de imagem para identificação de doenças de plantas e recomendações de tratamento
- **📊 Informações de Preço de Mercado**: Dados de preço de culturas em tempo real e tendências de mercado
- **🏛️ Programas Governamentais**: Informações sobre subsídios agrícolas, programas e benefícios para agricultores
- **🗣️ Suporte a Mensagens de Voz**: Processamento de mensagens de áudio com transcrição automática
- **🌐 Suporte Multilíngue**: Serviços de tradução para suporte a idiomas regionais
- **📚 Base de Conhecimento**: Banco de dados abrangente de conhecimento agrícola
- **💬 Memória de Conversação**: Mantém o histórico de bate-papo para aconselhamento agrícola personalizado
- **📱 Integração com Telegram**: Integração perfeita com a API do Telegram
- **🔒 Comunicação Segura**: Verificação de assinatura HMAC para webhooks seguros (se aplicável ao Telegram)
- **🎯 Validação de Resposta**: Garantia de qualidade para aconselhamento agrícola gerado por IA

## Estrutura do Projeto 📁

AssisIAgro/
├── app/
│   ├── init.py              # Flask app factory
│   ├── config.py                # Configuration management
│   ├── views.py                 # Webhook endpoints
│   ├── decorators/
│   │   └── security.py          # Security decorators
│   ├── services/
│   │   ├── gemini_service.py    # Integração Gemini AI para consultas agrícolas
│   │   ├── conversation_service.py # Gerenciamento do histórico de conversas
│   │   ├── knowledge_base_service.py # Banco de dados de conhecimento agrícola
│   │   ├── prompt_manager.py    # Prompts agrícolas especializados
│   │   ├── response_validator.py # Validação de qualidade para aconselhamento agrícola
│   │   ├── translation_service.py # Suporte multilíngue
│   │   ├── speech_service.py    # Processamento de fala para texto
│   │   └── openai_service.py    # Serviço de IA alternativo
│   └── utils/
│       ├── telegram_utils.py    # Utilitários e processamento de mensagens do Telegram
│       └── whatsapp_utils.py    # Utilitários e processamento de mensagens do WhatsApp (se ainda em uso)
├── data/
│   ├── crop_diseases.json       # Banco de dados de doenças de culturas
│   ├── government_schemes.json  # Programas e subsídios agrícolas
│   ├── kisan_knowledge_base.json # Conhecimento agrícola abrangente
│   └── market_prices.json       # Informações de preço de mercado
├── start/                       # Exemplos de início rápido e ferramentas de teste
├── debug_whatsapp.py            # Ferramenta de solução de problemas da API do WhatsApp
├── configurar_telegram_webhook.py # Script para configurar o webhook do Telegram
├── run.py                       # Ponto de entrada da aplicação
├── requirements.txt             # Dependências
├── .env.sample                  # Modelo de ambiente
├── .gitignore                   # Regras de ignorar do Git
└── README.md                    # Este arquivo


## Instruções de Configuração 🚀

### Pré-requisitos

- Python 3.7+
- Conta da API do Telegram (ou WhatsApp Business API se aplicável)
- Chave da API do Google Gemini (ou chave da API OpenAI)
- ngrok (para desenvolvimento local)
- ffmpeg (para processamento de áudio) - [Baixe aqui](https://ffmpeg.org/download.html)

### Instalação

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/Jay7568/AssisIAgro.git](https://github.com/Jay7568/AssisIAgro.git)
    cd AssisIAgro
    ```

2.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuração do Ambiente**
    Copie o arquivo de ambiente de exemplo e configure-o:
    ```bash
    cp .env.sample .env
    ```

    Edite o arquivo `.env` com suas credenciais:
    ```env
    # Configuração do Telegram Bot API
    TELEGRAM_BOT_TOKEN=seu_token_do_telegram_bot

    # Configuração de IA
    GEMINI_API_KEY=sua_chave_api_do_gemini
    GEMINI_MODEL=models/gemini-1.5-flash
    GEMINI_VISION_MODEL=gemini-pro-vision

    # Opcional: Configuração OpenAI
    # OPENAI_API_KEY=sua_chave_api_do_openai
    # OPENAI_ASSISTANT_ID=seu_assistant_id

    # Configurações da Aplicação
    FLASK_ENV=development
    DEBUG=True
    ```

4.  **Execute a aplicação**
    ```bash
    python run.py
    ```

5.  **Configure o Webhook do Telegram (para produção/Render)**
    ```bash
    python configurar_telegram_webhook.py
    ```
    (Você precisará da URL pública do seu bot no Render para isso)

## Configuração da API do Telegram 📱

### 1. Crie um Bot no BotFather
- No Telegram, procure por `@BotFather`.
- Use o comando `/newbot` para criar um novo bot.
- Ele lhe dará um `TELEGRAM_BOT_TOKEN`.

### 2. Configure o Webhook
- A URL do webhook será a URL pública do seu serviço no Render (ex: `https://assis-iagro-bot.onrender.com/webhook`).
- Use o script `configurar_telegram_webhook.py` para definir o webhook.

## Configuração do Serviço de IA 🧠

### Gemini AI para Agricultura (Padrão)
O bot usa a IA Gemini do Google com prompts agrícolas especializados e base de conhecimento:

1.  Obtenha a chave da API em [Google AI Studio](https://makersuite.google.com/app/apikey)
2.  Adicione `GEMINI_API_KEY` ao seu arquivo `.env`
3.  O sistema usa prompts especializados para:
    - Identificação de doenças em culturas
    - Melhores práticas agrícolas
    - Consultas de preço de mercado
    - Informações sobre programas governamentais
    - Aconselhamento agrícola relacionado ao clima

### Base de Conhecimento Agrícola
O bot inclui dados abrangentes para a agricultura:
- **Doenças de Culturas**: Mais de 500 entradas de doenças com sintomas e tratamentos
- **Programas Governamentais**: Últimos subsídios agrícolas e benefícios para agricultores
- **Preços de Mercado**: Informações de preços de culturas em tempo real
- **Conhecimento Agrícola**: Melhores práticas, conselhos sazonais e dicas de cultivo

### OpenAI (Alternativa)
Para usar OpenAI em vez disso:
1.  Descomente a importação do OpenAI em `app/services/gemini_service.py` (ou onde for relevante)
2.  Comente a importação do Gemini
3.  Configure as credenciais do OpenAI em `.env`
4.  Nota: A especialização agrícola pode exigir engenharia de prompt adicional

### Configuração de Fala para Texto
O bot suporta processamento de mensagens de áudio com conversão automática de formato:

1.  **Google Cloud Speech** (recomendado para melhor qualidade):
    - Habilite a API Google Cloud Speech-to-Text
    - Configure as credenciais da conta de serviço
    - Suporta formatos OGG, WAV, FLAC diretamente

2.  **SpeechRecognition** (fallback de camada gratuita):
    - Usa o serviço gratuito de reconhecimento de fala do Google
    - Converte automaticamente formatos de áudio usando ffmpeg

3.  **Suporte a Formatos de Áudio**:
    - OGG (formato padrão do WhatsApp/Telegram para áudio)
    - WAV, FLAC, MP3
    - Conversão automática para formatos não suportados

## Depuração e Solução de Problemas 🔧

### Ferramenta de Solução de Problemas da API
Use o script de depuração integrado para testar sua configuração da API do WhatsApp (se ainda estiver usando):

```bash
python debug_whatsapp.py
Este script irá:

✅ Testar conectividade e permissões da API

🔑 Validar tokens de acesso e escopos

📱 Verificar configuração do número de telefone

📤 Enviar mensagens de teste (opcional)

🔍 Fornecer diagnósticos de erro detalhados

Problemas Comuns e Soluções
401 Não Autorizado: Token expirado ou inválido - gere novo token

Escopos ausentes: Garanta que o token tenha a permissão necessária

Erros de processamento de áudio: Instale ffmpeg para conversão de formato de áudio

Limitação de taxa: Implemente a limitação de taxa de solicitação adequada

Funcionalidades em Detalhe 🔍
Inteligência Agrícola
Aconselhamento de Culturas: Aconselhamento especializado para diferentes culturas e estágios de cultivo

Diagnóstico de Doenças: Identificação de doenças de plantas baseada em IA a partir de imagens

Integração Climática: Recomendações agrícolas conscientes do clima

Orientação Sazonal: Aconselhamento oportuno com base nas estações agrícolas

Manejo do Solo: Recomendações de saúde do solo e fertilizantes

Inteligência de Mercado
Rastreamento de Preços: Preços de mercado em tempo real para várias culturas

Tendências de Mercado: Análise histórica de preços e previsão

Melhores Momentos de Venda: Momento ideal para vendas de culturas

Variações Regionais: Informações de mercado específicas da localização

Assistência a Programas Governamentais
Descoberta de Programas: Encontre programas governamentais relevantes para agricultores

Verificação de Elegibilidade: Determine a qualificação para vários programas

Orientação de Aplicação: Assistência passo a passo para aplicação

Informações sobre Subsídios: Detalhes sobre subsídios agrícolas

Memória de Conversação e Personalização
Armazena histórico de cultivo e preferências por usuário

Mantém o contexto em várias conversas

Recomendações personalizadas com base no perfil do agricultor

Acompanha ciclos de cultivo e fornece lembretes oportunos

Suporte Multilíngue
Serviços de Tradução: Tradução automática para idiomas regionais

Processamento de Voz: Fala para texto em vários idiomas

Contexto Cultural: Aconselhamento agrícola culturalmente apropriado

Terminologia Local: Usa termos agrícolas específicos da região

Análise de Imagem para Agricultura
Avaliação da Saúde da Cultura: Análise visual das condições das plantas

Detecção de Doenças: Identificação automatizada de doenças de plantas

Deficiência de Nutrientes: Detecção de deficiências nutricionais em culturas

Identificação do Estágio de Crescimento: Determinação dos níveis de maturidade da cultura

Garantia de Qualidade
Validação de Resposta: Garante a precisão do aconselhamento agrícola

Verificação da Base de Conhecimento: Referência cruzada com bancos de dados agrícolas

Integração de Revisão por Especialistas: Opção para validação por especialistas de conselhos críticos

Aprendizado Contínuo: Melhora as respostas com base no feedback do agricultor

Endpoints da API 🔗
GET /webhook
Endpoint de verificação de webhook para a API do Telegram (e WhatsApp Business API, se aplicável)

POST /webhook
Recebe mensagens de entrada do Telegram (e WhatsApp, se aplicável) e as processa

Desenvolvimento 💻
Desenvolvimento Local com ngrok
Bash

# Instale ngrok
# Execute seu aplicativo Flask
python run.py

# Em outro terminal, exponha o servidor local
ngrok http 8000

# Use a URL do ngrok como sua URL de webhook no BotFather (Telegram) ou Meta Developer Console (WhatsApp)
Testando Funcionalidades Agrícolas
O bot inclui exemplos de início rápido especializados:

gemini_quickstart.py - Teste a integração de IA agrícola

whatsapp_quickstart.py - Teste a API do WhatsApp

assistants_quickstart.py - Teste o Assistente OpenAI

Teste funcionalidades agrícolas:

Bash

# Teste a detecção de doenças em culturas
python -c "from app.services.gemini_service import generate_response_with_image; print('Detecção de doenças pronta')"

# Teste a base de conhecimento
python -c "from app.services.knowledge_base_service import search_knowledge_base; print('Base de conhecimento carregada')"

# Teste o serviço de tradução
python -c "from app.services.translation_service import translation_service; print('Serviço de tradução pronto')"
Use a ferramenta de depuração para testes abrangentes da API:

Bash

python debug_whatsapp.py
Implantação 🚀
Considerações de Produção para IA Agrícola
Use variáveis de ambiente para todos os dados sensíveis

Habilite HTTPS para endpoints de webhook

Configure o registro e monitoramento adequados para consultas agrícolas

Configure o rastreamento de erros e alertas para aconselhamento agrícola crítico

Use um servidor WSGI de produção (ex: Gunicorn)

Implemente limitação de taxa para chamadas de API

Configure a limpeza adequada de arquivos de áudio e imagem

Atualizações regulares para a base de conhecimento agrícola

Faça backup de históricos de conversas e dados de agricultores

Implemente medidas de privacidade de dados para informações de agricultores

Exemplos de Comandos de Implantação
Bash

# Usando Gunicorn para produção
gunicorn -w 4 -b 0.0.0.0:8000 run:app

# Usando Docker (crie Dockerfile)
docker build -t assis-iagro .
docker run -p 8000:8000 assis-iagro

# Para alta disponibilidade com dados agrícolas
gunicorn -w 4 -b 0.0.0.0:8000 --timeout 120 run:app
Casos de Uso 🚜
Para Agricultores
Identificação de Doenças em Culturas: "Minhas plantas de tomate estão com manchas amarelas. O que há de errado?"

Consultas de Preço de Mercado: "Qual o preço atual do trigo em [Nome da Região]?"

Informações sobre Programas Governamentais: "Existem subsídios para irrigação por gotejamento?"

Aconselhamento Baseado no Clima: "Devo plantar arroz esta semana, considerando o clima?"

Manejo de Pragas: "Como controlo pulgões na minha cultura de algodão?"

Para Extensionistas Agrícolas
Referência Rápida: Acesso a um banco de dados agrícola abrangente

Diagnóstico Visual: Identificação de problemas de culturas baseada em imagens

Atualizações de Programas: Últimas informações sobre programas governamentais

Suporte Multi-idioma: Comunicação com agricultores em idiomas locais

Para Negócios Agrícolas
Inteligência de Mercado: Monitoramento de preços de culturas em tempo real

Engajamento do Agricultor: Canal de comunicação direto com a comunidade agrícola

Recomendações de Produtos: Sugestões de produtos agrícolas conscientes do contexto

Coleta de Dados: Insights sobre desafios e necessidades agrícolas

Idiomas Suportados 🌐
Português (Brasil)

Hindi (हिंदी)

Marathi (मराठी)

Gujarati (ગુજરાતી)

Punjabi (ਪੰਜਾਬੀ)

Bengali (বাংলা)

Tamil (தமிழ்)

Telugu (తెలుగు)

Kannada (ಕನ್ನಡ)

Malayalam (മലയാളം)

Inglês

Fontes de Dados 📊
Base de Conhecimento Agrícola
Variedades de Culturas: Mais de 200 variedades de culturas com detalhes de cultivo

Banco de Dados de Doenças: Mais de 500 doenças com sintomas e tratamentos

Informações sobre Pragas: Pragas agrícolas comuns e medidas de controle

Programas Governamentais: Banco de dados atualizado de programas centrais e estaduais

Dados de Mercado: Integração com plataformas de mercado agrícola

Integração Climática: Conexão com serviços meteorológicos

Personalização Regional
Recomendações de culturas específicas do estado

Variações regionais de preços de mercado

Disponibilidade de programas governamentais locais

Aconselhamento apropriado para a zona climática

Integração de práticas agrícolas tradicionais

Contribuição 🤝
Faça um fork do repositório

Crie uma branch de funcionalidade (git checkout -b feature/nova-funcionalidade)

Faça seus commits (git commit -m 'Adiciona funcionalidade incrível')

Envie para a branch (git push origin feature/nova-funcionalidade)

Abra um Pull Request

Licença 📄
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

Suporte 💬
Para perguntas e suporte:

Crie uma issue no GitHub

Verifique a documentação da API do Telegram

Revise a documentação da IA Gemini do Google

Agradecimentos 🙏
Google pela API Gemini AI e capacidades de IA agrícola

Telegram pela API do Bot

Comunidade Flask pelo excelente framework

[Nome da Instituição de Pesquisa Agrícola Local/Nacional, se houver] para dados agrícolas

Universidades Estaduais de Agricultura para conhecimento regional

Comunidades de agricultores para feedback e testes no mundo real

Extensionistas agrícolas para expertise no domínio

OpenAI para opções de integração de IA alternativas

Nota: Este assistente de IA agrícola foi projetado para apoiar os agricultores com informações e conselhos. Sempre consulte especialistas agrícolas locais para decisões críticas de cultivo. O bot visa democratizar o acesso ao conhecimento agrícola, respeitando a sabedoria tradicional de cultivo e as práticas locais.

Começando para Agricultores 👨‍🌾
Como Usar o AssisIAgro
Adicione o Bot no Telegram: Procure o seu bot pelo nome de usuário no Telegram

Envie uma Mensagem: Comece com "Olá" ou "Oi" para iniciar a conversa

Faça Perguntas: Use linguagem simples para perguntar sobre tópicos agrícolas

Envie Imagens: Tire fotos de culturas, doenças ou pragas para análise

Mensagens de Voz: Fale no seu idioma preferido para consultas de voz

Exemplos de Conversas
Consulta de Doença em Cultura:

Agricultor: "Minhas plantas de tomate estão com manchas marrons nas folhas"
AssisIAgro: "Isso parece ser a doença 'Requeima' (early blight). Aqui está o que você pode fazer:
🍅 Remova as folhas afetadas imediatamente
💧 Reduza a rega por cima
🌿 Aplique um fungicida à base de cobre
📅 Pulverize a cada 7-10 dias até que os sintomas desapareçam"
Consulta de Preço de Mercado:

Agricultor: "preço do trigo hoje"
AssisIAgro: "Preços atuais do trigo (referência):
🌾 Trigo Comum: R$ X.XX/saca
🌾 Trigo Duro: R$ Y.YY/saca
📍 Mercado mais próximo: [Nome do Mercado], [Distância]
📈 Tendência de preço: Estável (+2% em relação ao mês passado)"
Informações sobre Programa Governamental:

Agricultor: "subsídio para bomba solar"
AssisIAgro: "Subsídios disponíveis para bomba solar:
☀️ Programa [Nome do Programa]: Z% de subsídio
📋 Elegibilidade: Todos os agricultores com terra agrícola
💰 Subsídio máximo: R$ A.AAA para bomba de B HP
📝 Solicite em: Escritório agrícola mais próximo
📞 Linha de ajuda: [Número de Telefone]"
```

##  Demo Video
Watch our project demonstration: [AssiIAgro Demo](https://youtu.be/aI2OE6n8ZCI)
=======
# AssisIAgro
Chatbot de Telegram com IA Gemini para agricultura
>>>>>>> a4eb9e65a2b4f2ed67118508a96b2910532c1430
