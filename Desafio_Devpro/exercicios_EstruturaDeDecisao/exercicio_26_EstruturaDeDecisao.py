'''
26 - Um posto está vendendo combustíveis com a seguinte tabela de 
     descontos:
    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço 
do litro da gasolina é R$ 2,50 o
preço do litro do álcool é R$ 1,90.
Mostre o restultado com duas casas decimais
'''
preco_g = 2.5
preco_a = 1.9
quantidade = 0
combustivel = ''

while True:
    try:

        while 'G' != combustivel != 'A': 
            combustivel = input('Qual o combustível? (A) - álcool ou (G) - gasolina? ').upper()
        while quantidade <= 0:
            quantidade = float(input('Quantos litros? '))

        if combustivel == 'A':
            tipo_combustivel = 'álcool'
            if quantidade <= 20:
                desconto = 3
            else:
                desconto = 5
            preco_a_com_desconto = preco_a - (preco_a * (desconto/100))

            valor_pagar = quantidade * preco_a
            valor_pagar_desconto = quantidade * preco_a_com_desconto

        if combustivel == 'G':
            tipo_combustivel = 'gasolina'
            if quantidade <= 20:
                desconto = 4
            else:
                desconto = 6
            preco_g_com_desconto = preco_g - (preco_g * (desconto/100))

            valor_pagar = quantidade * preco_g
            valor_pagar_desconto = quantidade * preco_g_com_desconto

        print(f'{quantidade} litro(s) de {tipo_combustivel}', end = '')
        print(f' custa(m): R$ {valor_pagar:.2f}. Com {desconto}% de desconto, fica R$ {valor_pagar_desconto:.2f}')
        break
    except ValueError:
        #print('Entrada invalida!!!') 