import json

# Lê a lista de faturamento diário em formato JSON
with open('/questao3/dados.json', 'r') as f:
    faturamento_diario = json.load(f)

# Calcula o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calcula a média mensal de faturamento diário, ignorando os dias sem faturamento
soma_faturamento = sum(faturamento_diario)
num_dias_com_faturamento = len([f for f in faturamento_diario if f > 0])
media_mensal = soma_faturamento / num_dias_com_faturamento

# Conta o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_media = len([f for f in faturamento_diario if f > media_mensal])

# Imprime os resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)
