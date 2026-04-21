# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
google-generativeai
pandas
python-dotenv
```

## Como Rodar

```
1. Clone o repositório.
2. Crie um arquivo `.env` na raiz com sua `GOOGLE_API_KEY`.
3. Instale as dependências:
   ```bash
   pip install -r src/requirements.txt

# Rodar a aplicação
streamlit run src/app.py
```
