# 📦 Dashboard de Desempenho Logístico — 2025 (Dados Sintéticos)

Este projeto apresenta um **dashboard completo de performance logística**, construído com **Power BI**, utilizando **dados totalmente sintéticos** para simular um cenário real de operação.

O objetivo é demonstrar **domínio em análise de dados, visualização, lógica de indicadores e storytelling analítico** aplicado ao contexto de logística e supply chain.

---

## 🚛 Objetivo do Projeto

Criar um painel que responda a perguntas-chave da operação logística, como:

- Quais são as transportadoras responsáveis pela maior parte do volume?
- Como está o frete distribuído por fornecedor?
- Quais tipos de veículos mais carregam?
- Há sazonalidade ou tendência nos carregamentos mensais?
- Como está a pontualidade?
- Quais os principais destinos?

Tudo isso usando uma base **fictícia**, mas estruturada de forma fiel a uma operação real.

---

## 🧱 Estrutura do Projeto

📁 dashboard-logistica-cargas/
│
├── 📁 data/
│ ├── dados_sinteticos_cargas.xlsx # Base artificial usada no dashboard
│
├── 📁 powerbi/
│ ├── dashboard_logistica.pbix # Arquivo do Power BI
│
├── 📁 img/
│ ├── preview_dashboard.png # Screenshot do painel
│
└── README.md

---

## 📊 Destaques do Dashboard

- **Pareto 80/20 de Volume por Transportadora**
- **Pareto 80/20 de Frete por Transportadora**
- **Distribuição de Carregamentos por Tipo de Veículo**
- **Tendência mensal de carregamentos**
- **Mapa interativo com principais destinos**
- **KPI de pontualidade**

---

## 🧪 Como os Dados Sintéticos Foram Gerados

Os dados foram criados utilizando Python, com:

- Distribuições proporcionais realistas (ex.: 80/20 entre transportadoras)
- Campos típicos de operação logística:
  - Transportadora
  - Tipo de veículo
  - Cidade / Estado
  - Data do carregamento
  - Quantidade de caixas
  - Valor de frete
  - Indicador de pontualidade
- Volume simulado: ~15 milhões de caixas
- Frete agregado simulado: ~40 milhões

📌 *Nenhuma informação, estrutura ou valor real da empresa foi utilizado.*

---

## 🛠️ Tecnologias Utilizadas

- **Power BI**
- **Python (para gerar dados sintéticos)**
- **Pandas**
- **NumPy**
- **Matplotlib / Seaborn (validação dos dados)**

---

## ▶️ Como Reproduzir

1. Baixe o arquivo `.pbix` na pasta `powerbi/`.
2. Abra no Power BI Desktop.
3. Os dados sintéticos estão na pasta `data/`.
4. Você pode editar o modelo, trocar parâmetros ou gerar novos dados.

---

## 🚀 Possíveis Extensões

- Previsão de demanda com Prophet ou ARIMA
- Dashboard de performance de transportadoras com ranking por KPI
- Criação de API fake servindo dados logísticos
- Versão web do dashboard usando Streamlit

---

## 📚 Lições Aprendidas

- Boa parte da operação logística pode ser resumida em poucos KPIs estratégicos.
- Visualizações simples (Pareto, linha, barra e gauge) contam histórias poderosas.
- A criação de dados sintéticos é essencial para portfólios profissionais na área.
- Power BI + Python formam um combo forte para projetos de supply chain.

---

## 📸 Preview

> Cole aqui a imagem do dashboard  
`img/preview_dashboard.png`

---

## ✉️ Contato

[LinkedIn — Leonardo Souza Coelho](https://www.linkedin.com/in/leoscoelho/)

Projetos de dados, logística, automação e IA.
