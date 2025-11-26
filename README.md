# Sistema de Controle de Estoque - Integração com Clima

Aplicação Flask com SQLite para controlar itens de estoque e preparar a integração com previsão do tempo (OpenWeatherMap). A interface segue a identidade visual inspirada na Petzoo.

## Requisitos

- Python 3.11+
- Virtualenv (recomendado)

## Instalação e execução

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\\Scripts\\activate   # Windows PowerShell
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Inicialize o banco com valores padrão (cidade e mensagens iniciais):
   ```bash
   flask --app run.py init-db
   ```
4. Suba a aplicação:
   ```bash
   python run.py
   ```
5. Acesse `http://127.0.0.1:5000` no navegador para usar o painel.

## Telas e funcionalidades

- **Dashboard**: mostra a cidade monitorada, o fator de impacto da chuva e as mensagens configuradas para tempo ensolarado ou chuvoso. Inclui atalho para editar configurações e link para obter a API key do OpenWeatherMap.
- **Itens (Estoque)**: lista os itens cadastrados com categoria, unidade, estoque atual/mínimo e observações. Permite criar novo item, editar registros existentes ou removê-los por meio de ações rápidas na tabela.
- **Movimentações**: planejada para registrar entradas e saídas de estoque; ainda não há fluxo implementado na interface nesta etapa inicial.
