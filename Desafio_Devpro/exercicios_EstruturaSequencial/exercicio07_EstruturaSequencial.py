'''
07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre 
o dobro desta área para o usuário.

'''

lado = float(input('Informe a medida do lateral do quadrado: '))

area_quadrado = lado ** 2
print(f'A área do quadrado com esse lado é: {area_quadrado:,.2f}')
print(f'O dobro da aŕea do quadrado é: {(area_quadrado * 2):,.2f}')
