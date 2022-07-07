'''
12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule
 seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 





while True:
    try:
        altura = float(input('Informe a altura em metros: '))
        peso_ideal = (72.7*altura) - 58
        print(f'O peso ideal para uma pessoa com altura de {altura} metros é : {peso_ideal:.1f}')
        break    
    except ValueError:
        print('Valor inválido!!!')
'''

while True:
    try:
        altura = float(input('Informe a altura em metros: '))
        peso_ideal = (72.7*altura) - 58
        # print(f'O peso ideal para uma pessoa com altura de {altura} metros é : {peso_ideal:,.2f}')
        print(f'Seu peso ideal é {peso_ideal:.1f} kg ')
        break    
    except ValueError:
        print('Valor inválido!!!')


