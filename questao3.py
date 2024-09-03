import json

arquivo_json = 'faturamento.json'

with open('faturamento.json', 'r') as file:
    dados = json.load(file)


faturamento_validos = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)

media_mensal = sum(faturamento_validos) / len(faturamento_validos)


dias_acima_da_media = sum(1 for f in faturamento_validos if f > media_mensal)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média mensal: {dias_acima_da_media}")
