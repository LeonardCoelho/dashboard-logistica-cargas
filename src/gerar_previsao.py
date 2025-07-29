import pandas as pd
from datetime import datetime, timedelta
import random

# 1. Ler Excel e aba correta
df = pd.read_excel('Dados_Cargas_2024.xlsx', sheet_name='Cargas')
df.columns = df.columns.str.strip().str.upper()

# 2. Converter DATA
df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True)

# 3. Criar coluna SEMANA como início da semana
df['SEMANA'] = df['DATA'].dt.to_period('W').apply(lambda r: r.start_time)

# 4. Agrupar por SEMANA + colunas-chave
df_semanal = df.groupby([
    'SEMANA', 'CD ORIGEM', 'DESTINO', 'UF', 'CLIENTE', 'PERFIL'
]).agg({'ROMANEIO': 'count'}).reset_index().rename(columns={'ROMANEIO': 'QTD_CARREGAMENTOS'})

# 5. Ajustar datas para 2025 mantendo padrão de semana
def ajustar_para_2025(data_2024):
    dias_passados = (data_2024 - datetime(2024, 1, 1)).days
    base_2025 = datetime(2025, 1, 1)
    return base_2025 + timedelta(days=dias_passados)

df_semanal['DATA_2025'] = df_semanal['SEMANA'].apply(ajustar_para_2025)

# 6. Calcular semana do mês (só número) e nome do mês
def semana_do_mes(data):
    primeiro_dia_mes = data.replace(day=1)
    inicio_semana = primeiro_dia_mes - timedelta(days=primeiro_dia_mes.weekday())
    return ((data - inicio_semana).days // 7) + 1

nomes_meses_pt = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

df_semanal['MÊS'] = df_semanal['DATA_2025'].dt.month.map(nomes_meses_pt)
df_semanal['SEMANA'] = df_semanal['DATA_2025'].apply(semana_do_mes)

# 7. Gerar +20% de linhas fictícias
qtd_extra = int(len(df_semanal) * 0.20)
linhas_extra = df_semanal.sample(n=qtd_extra, replace=True).copy()
linhas_extra.index = range(df_semanal.index.max() + 1, df_semanal.index.max() + 1 + qtd_extra)
linhas_extra['QTD_CARREGAMENTOS'] = (linhas_extra['QTD_CARREGAMENTOS'] * random.uniform(1.15, 1.25)).round().astype(int)

# 8. Unir e ordenar
df_final = pd.concat([df_semanal, linhas_extra], ignore_index=True)
df_final = df_final.sort_values(by=['MÊS', 'SEMANA']).reset_index(drop=True)

# 9. Selecionar colunas finais
df_final = df_final[[
    'SEMANA', 'MÊS', 'CD ORIGEM', 'DESTINO', 'UF', 'CLIENTE', 'PERFIL', 'QTD_CARREGAMENTOS'
]]

# 10. Exportar para Excel
df_final.to_excel('previsao_2025_semanal.xlsx', index=False)

print("✅ Arquivo gerado com sucesso: previsao_2025_semanal.xlsx")