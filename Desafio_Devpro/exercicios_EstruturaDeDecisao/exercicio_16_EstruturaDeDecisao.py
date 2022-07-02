'''
16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas
seguintes situações:

    ** Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não
      deve fazer pedir os demais valores, sendo encerrado;
    **Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre
      o programa;
    **Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    
    **Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''


import math
   
while True:
    try:
        a = float(input('Entre com o valor de a: '))
        if a == 0:
            print('Valor do coeficiente a deve ser diferente de 0')
            break
        b = float(input('Entre com o valor de b: '))
        c = float(input('Entre com o valor de c: '))
                
        delta = (b**2) - 4 * a * c
        
        if delta < 0:
           mensagem = 'Delta negativo ({delta:.0f}), por isso não existem raízes reais'
          
        elif delta == 0:
            raiz = (-b - math.sqrt(delta))/2 * a
            mensagem = f'Delta é 0, raíz única no valor de {raiz}'
        else:
            raiz = (-b - math.sqrt(delta))/2 * a
            raiz2 = (-b + math.sqrt(delta))/2 * a
            mensagem = f'Delta é {delta:.0f}, raízes são {raiz2} e {raiz}'
            
        print(mensagem)
        break
    
    except ValueError:
        print('Entrada inválida!!!')
        
    