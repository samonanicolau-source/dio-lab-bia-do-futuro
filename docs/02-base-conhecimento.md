# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Lembrar de dúvidas passadas e manter a continuidade do suporte. |
| `perfil_investidor.json` | JSON | Entender os objetivos do cliente (ex: reserva de emergência) e seu apetite a risco. |
| `produtos_financeiros.json` | JSON | Sugerir investimentos com explicações simples e sem "economês". |
| `transacoes.csv` | CSV | Categorizar gastos entre Essenciais e Lazer para sugerir a separação de contas. |
|'regras_higiene.json' | JSON | Fornecer diretrizes sobre métodos de organização (como o 50/30/20) e uso de contas digitais. |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

Os dados originais foram expandidos para suportar a proposta de Higiene Financeira:

[produtos_financeiros.json: Adição do campo explicacao_simples para traduzir termos técnicos para uma linguagem acessível.

transacoes.csv: Inclusão da coluna natureza_gasto (Fixo/Variável) para permitir uma análise de fluxo de caixa mais precisa.

regras_higiene.json: Criação de um novo dataset com dicas de boas práticas para separação de contas e organização de saldo em bancos digitais.]

---

## Estratégia de Integração

### Como os dados são carregados?

[Os arquivos JSON e CSV são carregados via biblioteca pandas e json no Python logo no início da execução. Eles são estruturados em dataframes ou dicionários para fácil consulta.]

### Como os dados são usados no prompt?

[Os dados são injetados dinamicamente no System Prompt. O agente recebe o perfil do cliente e o resumo das transações mais recentes como contexto imediato, permitindo que as respostas sejam personalizadas para a realidade financeira daquele usuário específico.]

---

## Exemplo de Contexto Montado


```
Contexto do Usuário:
- Nome: João Silva
- Perfil de Organização: Focado em Higiene Financeira (Contas separadas).
- Objetivo: Completar reserva de emergência até Junho/2026.

Análise de Gastos Recentes:
- Essenciais (Fixos): R$ 1.380,00 (Aluguel, Luz, etc.)
- Estilo de Vida (Variável): R$ 175,90 (Netflix, Restaurante)
- Sugestão Lumi: "Você ainda tem margem para mover R$ 200,00 para sua conta de reserva hoje.
...
```
