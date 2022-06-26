'''
17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida
     informe se este ano é ou não bissexto.
     
     
Para ser bissexto, o ano deve ser:

    Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

    Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

    Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o
    resto igual a zero.



'''




while True:
    try:
        ano_str = "11111"
        while len(ano_str) != 4:
            ano = int(input("Digite o ano que deseja consultar se é bissexto: "))
            ano_str = str(ano)
            # Só segue adiante recebendo 4 digitos. Recebendo letras cai em ValueError.
     

        quatro = ano % 4
        cem = ano % 100
        quatrocentos = ano % 400
                
        # primeira situação
        if quatro == 0:
            if cem != 0:  
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
                
        #segunda situação    
        if quatro != 0:
            if quatrocentos == 0: 
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
            
        #terceira condição
        if quatro != 0:
            if quatrocentos == 0:
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
        print(mensagem)
        
    except ValueError:
        print('Entrada inválida!!!')