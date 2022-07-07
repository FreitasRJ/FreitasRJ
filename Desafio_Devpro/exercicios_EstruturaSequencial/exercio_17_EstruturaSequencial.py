'''
Faça um Programa para uma loja de tintas. O programa

deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os
    respectivos preços em 3 situações:
        
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    considere latas cheias.


area_pintar = 100
rendimento = 6 por litro
cobertura_lata18 =  18 * rendimento
cobertura_lata3_6 =  3.6 * rendimento
quant18 =  area_pintar/cobertura_lata18
quant3_6 =  area_pintar/cobertura_lata3_6
'''

#Parametros
import math

rendimento = 6
valor_lata = 80
valor_galao = 25

area_pintar = float(input('Qual área a pintar em m²? '))
litros = (area_pintar/rendimento) * 1.1

lata = math.ceil(litros/18)
valor_lata = lata * 80

retorno_latas = f'Comprando só latas de 18,0 litros.' \
                f' R$ {valor_lata:,.2f}  por {lata} lata(s)'

galao = math.ceil(litros /3.6)
valor_galao = galao * 25

retorno_galao = f'Comprando só galões de 3,6 litros. R$' \
                f' {valor_galao:,.2f} por {galao} galao(oes).'

lata_18 = litros//18
lata18 = (litros /18)
lata18_valor = lata18 * 80
diferença = lata18 - (litros //18)
diferença = diferença * 18
diferença = math.ceil(diferença/3.6)

galao_completa_latas = diferença

if diferença > 0 and diferença <=  3.6:
    galao_completa_latas= 1
else:
    galao_completa_latas  =  math.ceil(galao_completa_latas/3.6)
valor_mescla_lata_galao = (lata18_valor) + (galao_completa_latas * 25)

retorno_lata_galao = f'Comprando latas e galões: R$ {valor_mescla_lata_galao:,.2f} por {lata_18} lata(s) e  {galao_completa_latas} galões.'

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('++                           RELATÓRIO                            ++')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(retorno_latas)
print(retorno_galao)
print(retorno_lata_galao)

#print(f'diferença: {diferença}')
#galoes = galao_completa_latas
#print(f'completa galoes: {galoes}')
