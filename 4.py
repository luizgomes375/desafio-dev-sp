# define os valores de faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calcula o valor total mensal da distribuidora
valor_total = sum(faturamento.values())

# calcula o percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentuais[estado] = (valor / valor_total) * 100

# imprime os percentuais de representação de cada estado
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
