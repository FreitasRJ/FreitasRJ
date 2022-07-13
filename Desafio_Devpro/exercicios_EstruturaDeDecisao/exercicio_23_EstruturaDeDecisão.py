'''
23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.

'''
while True:
    try:

        numero = float(input('digite um número: '))
        num = round(numero)
        if numero == num:
            print("'Inteiro'")
        else:
            print("'Decimal'") 
    except ValueError:
        print('Entrada inválida')
        