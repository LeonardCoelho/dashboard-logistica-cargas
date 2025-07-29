# 📊 Dashboard Previsão de Cargas 2025

Este projeto gera uma **previsão de cargas logísticas para o ano de 2025** com base em dados históricos de 2024. O objetivo é antecipar a demanda e permitir que transportadoras se programem com mais eficiência.

A previsão é feita com Python e os dados gerados alimentam um **dashboard interativo no Power BI** para visualização clara e estratégica.

---

## 🚚 Motivação

Na operação logística, prever o volume de cargas ajuda:

- Transportadoras a se organizarem com antecedência
- Equipes internas a tomarem decisões mais inteligentes
- Reduzir gargalos e atrasos operacionais

---

## 🔧 Tecnologias Utilizadas

- Python (Pandas, NumPy, etc.)
- Excel (entrada e saída dos dados)
- Power BI (dashboards)
- Jupyter Notebook

---

## 📁 Estrutura do Projeto

```
dashboard-previsao-cargas/
├── 📁 data/
│   └── dados_historicos_2024.xlsx
├── 📁 images/
│   └── exemplo_dashboard.png
├── 📁 src/
│   └── gerar_previsao.py
│   └── Dashboard.pbix
├── README.md
└── requirements.txt
```

---

## ⚙️ Lógica da Previsão

- Leitura dos dados históricos de 2024
- Aumento de 20% no volume de cargas, distribuído ao longo do ano
- Ajuste conforme padrão de dias da semana (operacionalmente relevante)
- Geração de nova base simulada para 2025
- Exportação para uso no Power BI

---

## 📊 Resultado

O Power BI conecta-se à base simulada e exibe:

- Previsão mensal e semanal de cargas
- Comparação entre 2024 e 2025
- Visualização por transportadora, cliente ou centro de distribuição

![Exemplo do dashboard](images/exemplo_dashboard.png)

---

## ▶️ Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/LeonardCoelho/dashboard-previsao-cargas.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script em `src/gerar_previsao.py`
4. Abra o dashboard Power BI apontando para a base gerada

---

## 📌 Observações

- O modelo não utiliza aprendizado de máquina, mas sim lógica de negócio com base em tendências reais
- Ideal para testes operacionais, simulações e planejamento estratégico

---

## 👤 Autor

**Leonardo Coelho**  
[GitHub](https://github.com/LeonardCoelho) · [LinkedIn](https://www.linkedin.com/in/leonardocoelho/)  
Campinas/SP

---

> Solução prática, feita sob pressão da operação e com visão estratégica. 🚀
