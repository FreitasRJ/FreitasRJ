'''
14 - Faça um programa que peça
 10 números inteiros, calcule e
 mostre a quantidade de números 
pares e a quantidade de números
 impares.



'''
def par_impar (nume):
    resp_par_imp = 'impar'
    testa = nume % 2
    if testa == 0:
        resp_par_imp = 'par'
    return resp_par_imp

try:
    conta = 1
    soma = 0
    while conta < 11:
        numero = int(input(f'Entre com o {conta}° número: '))
        soma += numero
        conta += 1
        print (par_impar (numero))
    
    print (soma)

 
       
except ValueError:
    print('Entrada inválida!!!')  