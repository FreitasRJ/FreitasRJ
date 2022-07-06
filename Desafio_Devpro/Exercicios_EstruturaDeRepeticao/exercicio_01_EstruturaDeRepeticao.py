'''
1 - Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor valido.
'''

while True:
    try:
        nota = 11
        while nota < 0 or nota > 10:
            nota = int(input('Entre com uma nota entre 0 e 10: '))
            if nota < 0 or nota > 10:
                print('Valor inválido!')
        break

    except ValueError:
        break

