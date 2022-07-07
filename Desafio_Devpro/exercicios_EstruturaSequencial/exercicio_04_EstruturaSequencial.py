'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.

'''
while True:
    try:
        nota = 0
        for _ in (1, 2, 3, 4):
            nota = nota + float(input(f'Informe a nota do bimestre {_}: '))
        print(f'A média anual é {nota / 4}')
        break
    except ValueError:
        print('Não foi digitado um número!!!')
        break
