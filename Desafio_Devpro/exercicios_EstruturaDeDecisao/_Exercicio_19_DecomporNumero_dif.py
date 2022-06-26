'''
Faça um Programa que leia um número inteiro menor que 1000
e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e",
    da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,
    305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''


exemplo = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16, 0]
   
for numero in exemplo:   
    #numero = int(input('Digite um numero entre (0 e 999): '))
    cent_str = dez_str = und_str = ''
    centenas, dezenas = divmod(numero,100)
    dezenas,unidades = divmod(dezenas,10)
    contNumero = 0
    resultado = ''
        
    # Trata centenas++++++++++++++
        
    if centenas == 1:
        cent_str = '1 centena'
        contNumero += 1
    elif centenas > 1:
        cent_str = str(centenas) + ' centenas'
        contNumero += 1
     # Trara dezenas++++++++++++++++
        
    if dezenas == 1:
        dez_str = '1 dezena'
        contNumero += 1
    elif dezenas > 1:
        dez_str = str(dezenas) + ' dezenas'
        contNumero += 1
        # Trara unidade++++++++++++++++
        
    if unidades == 1:
        und_str = '1 unidade'
        contNumero += 1
    elif unidades > 1:
        und_str = str(unidades) + ' unidades'
        contNumero += 1
            
        
        #print(cent_str+ dez_str + und_str)  
        #print(contNumero)
        
    if contNumero == 0:
        print('Zero. Não consta nada a declarar!!!')
        
        # Casos em que haja zero no valor declarado
        
                 
    if contNumero == 3:
        resultado = resultado = cent_str + ', ' + dez_str + ' e ' + und_str
        
    
    if contNumero == 1:
        if cent_str != '':
            resultado = cent_str
        elif dez_str != '':
            resultado = dez_str
        else:
            resultado = und_str
    
                    
    if contNumero == 2:
        if cent_str == '':
            resultado = dez_str + ' e ' + und_str
        if dez_str == '':
            resultado = cent_str + ' e ' + und_str
        if und_str == '':
            resultado = cent_str + ' e ' + dez_str
                    
    print(resultado)  
            
        
          
          
      
     
