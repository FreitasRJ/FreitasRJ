'''
16- Faça um programa que
 calcule o fatorial de um
número inteiro fornecido pelo
 usuário.

Ex.: 5!=5.4.3.2.1=120
'''
resultado = 0
try:
    numero = int(input('Digite o número que deseja saber o fatorial: '))
    conta = numero + 1
    print (f'{numero}!=', end = '')
    while conta >= 1:
        conta -= 1
        resultado += numero * (numero -1)
        if conta < numero and conta >= 1:
            print('.', end ='')
        if conta > 0:
            print(f'{conta}', end ='')

    print(f'={resultado}')

except ValueError:
    print('Entrada inválida!!!')