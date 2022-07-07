'''
09 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
     em graus Celsius.

    C = 5 * ((F-32) / 9).
'''
fah = float(input('Informe a temperatura em Fahrenheit a ser convertida em Celsius: '))
celsius = round( 5 * ((fah-32) / 9))
print(f'Essa temperatura é de {celsius} Celsius')
