'''
06 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

'''



while True:
    
    try:
        
        raio = float(input('Informe o raio do círculo a ser calculada a área: '))
        p = 3.1415
        area = p * (raio ** 2)
        print(f'A área do círculo com esse raio é: {area:,.2f}')

    except ValueError:
        print('Dado informado inválido!!!')
        
    