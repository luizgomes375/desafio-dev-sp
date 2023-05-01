import xml.etree.ElementTree as ET

# Carrega o arquivo XML e obtém o elemento raiz
tree = ET.parse('dados.xml')
root = tree.getroot()

# Inicializa uma lista para armazenar os valores de faturamento de cada dia
faturamentos = []

# Percorre todos os elementos "row" no arquivo XML
for dia in root.findall('row'):
    # Extrai o valor de faturamento do elemento "valor" e adiciona na lista de faturamentos
    valor = float(dia.find('valor').text)
    faturamentos.append(valor)

# Calcula o menor e o maior valor de faturamento diário utilizando as funções min() e max()
menor_valor = min(faturamentos)
maior_valor = max(faturamentos)

# Calcula a média mensal de faturamento, ignorando os dias sem faturamento
total_dias = len(faturamentos)
soma_faturamentos = sum(faturamentos)
media_mensal = soma_faturamentos / total_dias

# Calcula o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_media = len([valor for valor in faturamentos if valor > media_mensal])

# Imprime os resultados
print('Menor valor de faturamento diário:', menor_valor)
print('Maior valor de faturamento diário:', maior_valor)
print('Número de dias em que o valor de faturamento diário foi superior à média mensal:', dias_acima_media)
