"""
04 lista repetição
"""

populacao_a = 8000
populacao_b = 20000
taxa_cresc_a = .03
taxa_cresc_b = .015
ano = 0

while populacao_a <= populacao_b:
    ano += 1
    populacao_a += (populacao_a * taxa_cresc_a)
    populacao_b += (populacao_b * taxa_cresc_b)
    
print(f"Anos: {ano}")