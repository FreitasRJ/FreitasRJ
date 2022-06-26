'''
05 - Faça um Programa que converta metros para centímetros.

'''

while True:
    try:
        metro = float(input('Informe a medida em metros a ser convertida em centimetros: '))
        centimetro = metro * 100        
        print(f'Transformando para centímetros dá {centimetro} cm')
    except ValueError:
        print('Não informou um número!!!')
        

