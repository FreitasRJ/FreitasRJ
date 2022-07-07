'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.

'''

#from cgi import print_arguments

while True:
    try:

        num_i_01 = float(input('Entre com um número inteiro: '))
        num_i_02 = float(input('Entre com outro número inteiro: '))
        num_real = float(input('Entre com um número real: '))

        print(f'O produto do dobro do primeiro com metade do segundo é {(((num_i_01)*2) * (num_i_02/2)):.2f}')

        print(f'A soma do triplo do primeiro com o terceiro é {((3 * num_i_01) + num_real):.2f}')

        print(f'O terceiro elevado ao cubo é {(num_real ** 3):.2f}')

    except ValueError:

        print('Entrada inválida!!!')
