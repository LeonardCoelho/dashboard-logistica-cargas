# 🚛 Dashboard Logístico — Histórico e Previsão de Cargas

Este projeto une duas frentes fundamentais da logística: o acompanhamento do **histórico de cargas** e a **previsão de volume futuro**, usando ferramentas de análise de dados e visualização com foco operacional e estratégico.

📍 Desenvolvido com base em dados reais da operação logística, o dashboard entrega uma visão completa para apoiar a **gestão de pátio, transportadoras e planejamento de demanda**.

---

## 🎯 Objetivo

Criar um dashboard interativo que:

- Monitore indicadores logísticos em tempo real
- Detecte gargalos na operação (atrasos, filas, pátio, transportadoras)
- Projete o volume futuro de cargas com base em padrões históricos
- Apoie a tomada de decisões no curto e médio prazo

---

## 🧩 Estrutura do Dashboard

### 📄 Página 1 — Histórico de Cargas

> Visão analítica do que aconteceu na operação.

- Volume de cargas por mês, semana e dia
- Transportadoras com maior volume e atraso
- Tempo médio no pátio
- Cargas por cliente, rota ou perfil de veículo
- Análise de sazonalidade e picos de operação
- Filtros por data, centro de distribuição e tipo de carga

### 📈 Página 2 — Previsão de Cargas

> Estimativa de volume para os próximos dias com base em padrões históricos.

- Previsão diária para os próximos 30 dias
- Comparativo “Real x Previsto”
- Distribuição de cargas por dia da semana
- Gráfico de tendência (volume previsto vs. histórico)
- Projeção com base em média móvel ou modelos estatísticos (ex: Prophet, SARIMAX)

---

## 🛠️ Tecnologias Utilizadas

- **Power BI** — Visualização e interação
- **Excel** — Pré-processamento dos dados
- **Python (pandas / statsmodels / Prophet)** — Modelagem preditiva (opcional)
- **DAX** — Criação de medidas e KPIs
- **Power Query** — Transformações de dados

---

## 📁 Estrutura do Projeto

dashboard-logistica-cargas/
├── 📊 Dashboard.pbix # Arquivo Power BI com as duas páginas
├── 📁 data/ # Arquivos .xlsx usados no projeto
├── 📁 images/ # Prints do dashboard para preview
├── README.md

yaml
Copiar
Editar

---

## 🖼️ Preview do Dashboard

### Página 1 — Histórico de Cargas
![Histórico](images/historico.png)

### Página 2 — Previsão de Cargas
![Previsão](images/previsao.png)

---

## ✅ Benefícios para a Logística

- Antecipação de picos de volume e sobrecarga no pátio
- Redução de atrasos com gestão proativa
- Apoio à roteirização e escala de equipes
- Base para KPIs em tempo real e planejamento semanal

---

## 🧑‍💻 Autor

**Leonardo Coelho**  
Analista de Transportes | Estudante de Ciência de Dados  
📍 Campinas/SP  
📧 lnrds.coelho@gmail.com  
🔗 [GitHub](https://github.com/LeonardCoelho) | [LinkedIn](https://linkedin.com/in/leonardcoelho)
---

📌 Projeto real aplicado no contexto logístico para facilitar decisões no pátio, transporte e previ
