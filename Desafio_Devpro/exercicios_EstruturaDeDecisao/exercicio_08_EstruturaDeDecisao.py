'''
8 - Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.

Mostrar o resultado com duas casas decimais
'''


while True:
    try:
        preco_prod_01 = float(input('Entre com o valor do produto 01: '))
        preco_prod_02 = float(input('Entre com o valor do produto 02: '))
        preco_prod_03 = float(input('Entre com o valor do produto 03: '))
        
    except ValueError:
        
        print('Entrada inválida!!!')
        break
    
    if preco_prod_01 <= preco_prod_02:
        menor_preco = preco_prod_01
        
    if preco_prod_01 >= preco_prod_02:
        menor_preco = preco_prod_02
    
    if menor_preco > preco_prod_03:
        menor_preco = preco_prod_03
        
    
    print(f'Melhor produto custa R$ {menor_preco:,.2f}')
    break



   
