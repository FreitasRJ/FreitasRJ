'''
13 - Faça um programa que peça
 dois números, base e expoente,
 calcule e mostre o primeiro
 número elevado ao segundo 
número. Não utilize a função
 de potência da linguagem.

'''
try:

    base = 3
    expoente = 2
    resu = base
    controle = 1
    while controle < expoente:
        controle += 1
        resu = resu * base 
    print(resu)
       
except ValueError:
    print('Entrada inválida!!!')  