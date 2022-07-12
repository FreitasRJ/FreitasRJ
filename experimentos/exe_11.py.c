'''
11 - Altere o programa anterior
 para mostrar no final a soma 
dos números.



'''
try:
    
    num_1 = int(input('Entre com o primeiro número inteiro: '))
    num_2 = int(input('Entre com o segundo número inteiro: '))
    numero = num_1
    contador = num_1
    soma = 0
    while  num_1 <= contador < num_2 + 1:

        contador += 1
        soma += numero
        print (numero)
        numero += 1  
    print(soma)
except ValueError:
    print('Entrada inválida!!!')  