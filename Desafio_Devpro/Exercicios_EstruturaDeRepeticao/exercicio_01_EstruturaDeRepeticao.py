'''
1 - Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor valido.
'''

while True:
    try:
        nota = 11
        while nota < 0 or nota > 10:
            nota_str = input('Entre com uma nota entre 0 e 10: ')
            if not nota_str in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                print(f'Número inválido: {nota_str}')
            nota = int(nota_str)
        print(nota)

    except ValueError:
        break

