'''
07 repetição Faça um programa 
que leia 5 números e informe
 o maior número.
'''
try:
    maior = 0
    for a in range(1,6):
        numero = int(input(f'Informe o número {a}:  '))
        if numero > maior:
            maior = numero

    print(f'O maior número da lista é: {maior}')