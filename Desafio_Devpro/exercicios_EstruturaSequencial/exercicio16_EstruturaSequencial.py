'''
16 - Faça um programa para uma loja de tintas. O programa deverá pedir o 
     tamanho em metros quadrados da área a ser pintada. Considere que a cobertura
     da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em 
     latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de
     latas de tinta a serem compradas e o preço total.

'''
import math
rendimento = 3 # cada litro cobre 3 m²

while True:

     try:

          area_pintar = float(input('Informe a área a pintar em m²: '))
          area_cobertura_lata = 18 * rendimento
          quant_latas = math.ceil(area_pintar / area_cobertura_lata)
          valor_pagar = quant_latas * 80
          print(f'Para cobrir {area_pintar}m² ==>   {quant_latas} latas x R$ 80,00 = {valor_pagar}')
   
     except ValueError:

         print('Valor inválido!!!')

