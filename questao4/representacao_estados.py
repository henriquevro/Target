# Dicionário com o faturamento mensal por estado
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o faturamento total
faturamento_total = sum(faturamento_mensal.values())

# Calcula o percentual de representação de cada estado
for estado, faturamento in faturamento_mensal.items():
    percentual = faturamento / faturamento_total * 100
    print(f"{estado}: {percentual:.2f}%")