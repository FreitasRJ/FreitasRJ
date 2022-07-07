'''
13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
 calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 
'''

while True:
    try:
        h = float(input('Por favor informe sua altura: '))

        peso_ideal_h = (72.7 * h) - 58
     
        peso_ideal_m = (62.1 * h) - 44.7
    
        print(f'Seu peso ideal é {peso_ideal_m:.1f} kg, se você for mulher')
        print(f'Seu peso ideal é {peso_ideal_h:.1f} kg, se você for homem')
        
    
    except ValueError:
        print('Entrada inválida!!!')
        
