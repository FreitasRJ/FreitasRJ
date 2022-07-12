'''
6 - Faça um programa que imprima na tela os números de 1 a 20, um 
abaixo do outro. Depois modifique o
programa para que ele mostre os números um ao lado do outro.
'''

for contador in range(1,22):
    saida = ''
    for linha in range(1, contador):
        saida += str(linha) + ' '
    
    print(saida)