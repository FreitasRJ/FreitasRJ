'''
Faça um Programa que leia três números e mostre o maior deles.
'''


#print('Esse programa identifica o maior número entre três digitados')

while True:
    try:
        numero1 = 0
        numero2 = 0
        numero3 = 0
        maior = 0
        while numero1 == numero2 == numero3:
            numero1 = int(input('Entre com o primeiro número: '))
            numero2 = int(input('Entre com o segundo número: '))
            numero3 = int(input('Entre com o terceiro número: '))
        
      
        if numero1 >= numero2:
            maior = numero1
        if numero2 >= numero1:
            maior = numero2
        if numero3 >= maior:
            maior = numero3
         
        print(maior)   
        break        
    except ValueError:
        #print('Digite um número!!')
        break
                    