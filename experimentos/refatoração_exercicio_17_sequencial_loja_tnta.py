import math

rendimento = 6
valor_lata = 80
valor_galao = 25

area_pintar = float(input('Qual área a pintar em m²? '))
litros = math.ceil((area_pintar/rendimento) * 1.1)


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

print(f'Você deve comprar {litros:.2f} litros de tinta.')
print(f'Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.')
#    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
 #   Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
