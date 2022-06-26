'''
21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a
 valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas 
 disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
 de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na 
 máquina. 
 
 '''

# retorno = (nota100, nota_100_str, ', ', nota50, nota_50_str, ', ', nota10, nota_10_str, ', ', nota5, nota_5_str, ', ', nota1, nota_1_str)
# n100 + ', ' 
#          a

while True:
    try:
        
        nota_100 = nota_50 = nota_10 = nota_5 = nota_1 = 0   
        nota_100_str = nota_50_str = nota_10_str = nota_5_str = nota_1_str = saida = ""
        cont = saque = 0
    
        
       
        while saque < 1 or saque > 600:       
       
            saque = int(input('Limites para saque R$ 1 e R$ 600. Informe o valor do saque: '))
            
             
        retorno = [nota_100, nota_100_str, '', nota_50, nota_50_str, '', nota_10, nota_10_str, '', nota_5, nota_5_str, '', nota_1, nota_1_str]
  
            
    # -----------------------------------------------------
        nota_100, saque = divmod(saque, 100)
        if nota_100 != 0:
            retorno[1] = f'{nota_100} notas de R$ 100'
        
        
        nota_50, saque = divmod(saque, 50)
        if nota_50 != 0:
            retorno[4] = f'{nota_50} notas de R$ 50'
            
        nota_10, saque = divmod(saque, 10)
        if nota_10 != 0:
            retorno[7] = f'{nota_10} notas de R$ 10'
            
        nota_5, saque = divmod(saque, 5)
        if nota_5 != 0:
            retorno[10] = f'{nota_5} notas de R$ 5'
            
        nota_1 = saque 
        if nota_1 != 0:
            retorno[13] = f'{nota_1} notas de R$ 1'
        
        # sobre virgulas e e:
        # 1 1 1 1 1
        if nota_100 != 0 and nota_50 != 0 and nota_10 != 0 and nota_5 != 0 and nota_1 != 0:
            retorno[2] = retorno[5] = retorno[8] = ', '
            retorno[11] = ' e '
        # 1 0 0 0 1
        elif nota_100 != 0 and nota_50 == 0 and nota_10 == 0 and nota_5 == 0 and nota_1 != 0:
            #retorno[2] = retorno[5] = retorno[8] = ''
            retorno[11] = ' e '
        
        # 1 1 0 0 1
        elif nota_100 != 0 and nota_50 != 0 and nota_10 == 0 and nota_5 == 0 and nota_1 != 0:
            retorno[2]  = ', '
            retorno[11] = ' e '
            
        # 1 1 1 0 1
        elif nota_100 != 0 and nota_50 != 0 and nota_10 != 0 and nota_5 == 0 and nota_1 != 0:
            retorno[2] = retorno[5]  = ', '
            retorno[11] = ' e '
        
        # 0 1 1 1 1
        elif nota_100 == 0 and nota_50 != 0 and nota_10 != 0 and nota_5 != 0 and nota_1 != 0:
            #retorno[2] = ''
            retorno[5] = retorno[8] = ', '
            retorno[11] = ' e '
        
        # 0 0 1 1 1
        elif nota_100 == 0 and nota_50 == 0 and nota_10 != 0 and nota_5 != 0 and nota_1 != 0:
            #retorno[2] = retorno[5] = ''
            retorno[8] = ', '
            retorno[11] = ' e '
            
        # 0 0 0 1 1
        elif nota_100 == 0 and nota_50 == 0 and nota_10 == 0 and nota_5 != 0 and nota_1 != 0:
            retorno[11] = ' e '
        
        # 0 0 1 1 0
        elif nota_100 == 0 and nota_50 == 0 and nota_10 != 0 and nota_5 != 0 and nota_1 == 0:
            retorno[8] = ' e '

        # 0 0 1 0 1
        elif nota_100 == 0 and nota_50 == 0 and nota_10 != 0 and nota_5 == 0 and nota_1 != 0:
            retorno[11] = ' e '

        # 0 1 1 0 0
        elif nota_100 == 0 and nota_50 != 0 and nota_10 != 0 and nota_5 == 0 and nota_1 == 0:
            retorno[5] = ' e '
        
        # 1 1 0 0 0
        elif nota_100 != 0 and nota_50 != 0 and nota_10 == 0 and nota_5 == 0 and nota_1 == 0:
            retorno[2] = ' e '
            
        
        # 1 1 0 1 1
        elif nota_100 != 0 and nota_50 != 0 and nota_10 == 0 and nota_5 != 0 and nota_1 != 0:
            retorno[2]  = retorno[8] = ', '
            retorno[11] = ' e '
        # 1 0 1 1 1
        elif nota_100 != 0 and nota_50 == 0 and nota_10 != 0 and nota_5 != 0 and nota_1 != 0:
            retorno[2]  = retorno[8] = ', '
            retorno[11] = ' e '
        
        # 1 0 0 1 0
        elif nota_100 != 0 and nota_50 == 0 and nota_10 == 0 and nota_5 != 0 and nota_1 == 0:
            retorno[2] = retorno[5] = "+"
            retorno[8] = ' e '
            retorno[11] = ' + '
       
       
        # 1 0 0 1 1
        elif nota_100 != 0 and nota_50 == 0 and nota_10 == 0 and nota_5 != 0 and nota_1 != 0:
            retorno[8] = ', '
            retorno[11] = ' e '

        

        # 0 0 0 0 1
    
        # 0 0 0 1 0
        
        
        #print(retorno)
        
        while cont < 14:
            retorno_str = str(retorno[cont])
            if retorno_str != '' and retorno_str != '0':
                saida += retorno_str
            cont += 1
            
        print(saida)
         
        #break
    except ValueError:
        print('Entrada inválida!!!')
        
        
       
