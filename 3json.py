import json

# Lê o arquivo JSON
with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Inicializa as variáveis para cálculo das informações
soma_valores = 0
contador_dias = 0
menor_valor = float('inf')
maior_valor = float('-inf')

# Percorre os dados para calcular as informações
for dado in dados:
    # Verifica se o valor é menor ou maior do que os já encontrados
    valor = dado['valor']
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor

    # Soma o valor apenas se o dia não for final de semana ou feriado (dias úteis)
    if dado['dia'] % 7 not in (0, 6):
        soma_valores += valor
        contador_dias += 1

# Calcula a média mensal de faturamento
media_mensal = soma_valores / contador_dias

# Conta o número de dias em que o valor de faturamento diário foi superior à média mensal
contador_dias_acima_da_media = 0
for dado in dados:
    if dado['dia'] % 7 not in (0, 6):
        if dado['valor'] > media_mensal:
            contador_dias_acima_da_media += 1

# Imprime as informações calculadas
print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média mensal: {contador_dias_acima_da_media}")
