'''
10 -Faça um programa que receba 
dois números inteiros e gere os
 números inteiros que estão no
 intervalo compreendido por 
eles.

'''
try:
    
    num_1 = int(input('Entre com o primeiro número inteiro: '))
    num_2 = int(input('Entre com o segundo número inteiro: '))
    numero = num_1
    contador = num_1
    while contador >= num_1 and contador < num_2 + 1:

        contador += 1
        print (numero)
        numero += 1  
except ValueError:
    print('Entrada inválida!!!')  