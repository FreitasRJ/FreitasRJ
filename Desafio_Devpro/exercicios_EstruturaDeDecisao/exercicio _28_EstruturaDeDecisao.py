"""
Exercício 28 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5%
sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de 
carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da 
compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.

Mostre o restultado com duas casas decimais

saída doctest do curso: 
'8 kg de Picanha a R$ 7.80/kg saem a R$ 62.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 59.28'

'6 kg de Picanha a R$ 7.80/kg saem a R$ 46.80. Não há desconto, pagamento feito com dinheiro'

"""


while True:
    try:

        desconto_percentual = .05
        carne = ''

        print('Digite (f) para Filé duplo, (a) para Alcatra ou (p) para Picanha: ', end = '')
        
        while carne != 'f' and carne != 'a' and carne != 'p': 
            carne = input().lower()
          

        tipo_carne = "Filé Duplo"
        quantidade = 10
        forma_pagamento = "dinheiro"

        if forma_pagamento == 'dinheiro':

            preco_file = 4.90
            preco_Alcatra = 5.90
            preco_Picanha = 6.90
            
            if carne == "f": 
                preco_carne = preco_file
            elif carne == "a":
                preco_carne = preco_Alcatra
            elif carne == "p":
                preco_carne = preco_Picanha
                
        else:
            preco_file = 5.80
            preco_Alcatra = 6.80
            preco_Picanha = 7.80
            if carne == "f": 
                preco_carne = preco_file
            elif carne == "a":
                preco_carne = preco_Alcatra
            elif carne == "p":
                preco_carne = preco_Picanha
       


        valor_compra = quantidade * preco_carne
        if forma_pagamento == "dinheiro":
            print(f'{quantidade} kg de {tipo_carne} a R$ {preco_carne:.2f}/kg saem a R$ {valor_compra:.2f}. Não há desconto, pagamento feito com dinheiro')
        else: 
            valor_com_desconto = valor_compra - (valor_compra * desconto_percentual)
            print(f'{quantidade} kg de {tipo_carne} a R$ {preco_carne:.2f}/kg saem a R$ {valor_compra:.2f}. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_com_desconto:.2f}')    
        break
    except ValueError:
        break