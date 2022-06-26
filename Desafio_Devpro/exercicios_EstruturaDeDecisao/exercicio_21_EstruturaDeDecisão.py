
nota_100 = nota_50 = nota_10 = nota_5 = nota_1 = 1   
nota_100_str = nota_50_str = nota_10_str = nota_5_str = nota_1_str = saida = controle = ""
retorno = [nota_100, nota_100_str, '', nota_50, nota_50_str, '', nota_10, nota_10_str, '', nota_5, nota_5_str, '', nota_1, nota_1_str]


while True:
       
    try:
        
        nota_100 = nota_50 = nota_10 = nota_5 = nota_1 = 0   
        nota_100_str = nota_50_str = nota_10_str = nota_5_str = nota_1_str = ''
        saida = controle = ""
        cont = saque = 0
    
        
        while saque < 1 or saque > 600:       
            
            saque = int(input('Limites para saque R$ 1 e R$ 600. Informe o valor do saque: '))
                        
        retorno = [nota_100, nota_100_str, '', nota_50, nota_50_str, '', nota_10, nota_10_str, '',
                   nota_5, nota_5_str, '', nota_1, nota_1_str]
        retorno[0] = retorno[3] = retorno[6] = retorno[9] = retorno[12] = ''
            
    # -----------------------------------------------------
        nota_100, saque = divmod(saque, 100)
        if nota_100 != 0:
            retorno[1] = f'{nota_100} notas de R$ 100'
            controle += '1'
        else:
            controle += '0'
        
        nota_50, saque = divmod(saque, 50)
        if nota_50 != 0:
            retorno[4] = f'{nota_50} notas de R$ 50'
            controle += '1'
        else:
            controle += '0'
            
        nota_10, saque = divmod(saque, 10)
        if nota_10 != 0:
            retorno[7] = f'{nota_10} notas de R$ 10'
            controle += '1'
        else:
            controle += '0'
            
        nota_5, saque = divmod(saque, 5)
        if nota_5 != 0:
            retorno[10] = f'{nota_5} notas de R$ 5'
            controle += '1'
        else:
            controle += '0'
            
        nota_1 = saque 
        if nota_1 != 0:
            retorno[13] = f'{nota_1} notas de R$ 1'
            controle += '1'
        else:
            controle += '0'
               
# a variável controle representa se existem determinadas notas. Ex.: '10111' onde controle[0] indica existência
# de notas 100 se igual a 1 e inexistencia se igual a zero. Controle[1] o mesmo para as notas de 50 e assim  
# por diante: Quando saque igual a 166 gera controle igual a '11111", 165 gera '11110', 1 gera '00001'.
#-----------distribui as virgulas
        
        if int(controle[0]) + int(controle[1]) == 2:
            retorno[2] = ', '
        else:
            retorno[2] = ''

        if int(controle[1]) + int(controle[2]) == 2:
            retorno[5] = ', '
        else:
            retorno[5] = ''

        if int(controle[2]) + int(controle[3]) == 2:
            retorno[8] = ', '
        else:
            retorno[8] = ''

        if int(controle[3]) + int(controle[4]) == 2:
            retorno[11] = ', '
        else:
            retorno[11] = ''
        
                
#-----------------posiciona o ' e '.
               
        
        if controle[4] == '1':
            if controle[3] != '0' or controle[2] != '0' or controle[1] != '0' or controle[0] != '0':
                retorno[11] = ' e '
        
        elif controle[3] == '1' and controle[4] == '0':
            if controle[2] != '0' or controle[1] != '0' or controle[0] != '0':
                retorno[8] = ' e '
          
        
        elif controle[2] == '1' and controle[3] == '0' and controle[4] == '0':
            if controle[1] != '0' or controle[0] != '0':
                retorno[5] = ' e '
            
        elif controle[1] == '1' and controle[2] == '0' and controle[3] == '0' and controle[4] == '0':
            if controle[0] != '0':
                retorno[2] = ' e '
            
        
#--------Separa o conteudo que interessa da lista retorno e imprime a resposta.        
        a = 0
        while a < 14:
            if retorno[a] != '':
                saida += retorno[a]
            a += 1
        print()    
        print(saida)    
        for _ in range(4):
            print()
     
    except ValueError:
        print('Entrada inválida!!!') 