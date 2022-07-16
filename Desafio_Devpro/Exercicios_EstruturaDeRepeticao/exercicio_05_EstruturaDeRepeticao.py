'''
05 - Altere o programa anterior permitindo ao usuário informar as populações e 
as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 
'''

while True:
    try:
                
        populacao_a = int(input('Qual a população do país A? '))
        taxa_cresc_a = float(input('Qual a taxa, em percentagem, de crescimento do país A? '))
        taxa_cresc_a /= 100
        populacao_b = int(input('Qual a população do país B: '))
        taxa_cresc_b = float(input('Qual a taxa, em percentagem, de crescimento do país B? '))
        taxa_cresc_b /= 100
        if taxa_cresc_b > taxa_cresc_a:
            print(f'A taxa de crescimento do país B ({(taxa_cresc_b) * 100}%) deve ser menor do que a do país A ({(taxa_cresc_a) * 100}%)')
            break
        ano = 0

        while populacao_a <= populacao_b:
            ano += 1
            populacao_a += (populacao_a * taxa_cresc_a)
            populacao_b += (populacao_b * taxa_cresc_b)
            
        print(f'População de A, depois de {ano} ano(s) será de {populacao_a:.0f} pessoas, superando a de B, que será de {populacao_b:.0f} pessoas')
        break
    except ValueError:
        break