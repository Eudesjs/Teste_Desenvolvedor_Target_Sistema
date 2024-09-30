'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que
desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
import json

def calcular_faturamento(arquivo):
    with open(arquivo, "r") as f:
       dados = json.load(f)
    
    faturamentos = [item["valor"] for item in dados if item["valor"] > 0]

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)

    dias_acima_media = sum(1 for valor in faturamentos if valor > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media

arquivo = "Teste_Desenvolvedor_Target_Sistemas/dados.json"
menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(arquivo)

print(f"Maior Valor de Faturamento: R$ {maior_faturamento:.2f}")
print(f"Menor Valor de Faturmanento: R$ {menor_faturamento:.2f}")
print(f"Número de Dias com Faturamento acima de Média: R$ {dias_acima_media:.2f}")


