'''
2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
    Caso seja igual a 0, retorne None.
'''


while True:
    try:
        numero = float(input('Digite um número: '))
   
    except ValueError:
        print('Digite um número!!!') 
        break
    
    if numero > 0:
            num = 'Positivo'
    elif numero < 0:
            num = 'Negativo'
    else:
            num = 'não tem positivo nem negativo'
            
    print(num)
    
        
                
                
               