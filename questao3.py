import json

# Caminho para o arquivo JSON
arquivo_json = 'faturamento.json'

# Abrir e carregar o arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)


# Ignorar dias com faturamento zero
faturamento_validos = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Calcular o menor e o maior valor de faturamento
menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)

# Calcular a média mensal de faturamento
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

# Contar quantos dias o faturamento foi superior à média mensal
dias_acima_da_media = sum(1 for f in faturamento_validos if f > media_mensal)

# Exibir os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média mensal: {dias_acima_da_media}")
