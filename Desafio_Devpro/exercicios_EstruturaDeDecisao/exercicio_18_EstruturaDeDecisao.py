'''
18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data
válida.

'''
        


def ver_bissexto(ano):
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
    return mensagem
    

while True:
    try:
        aviso = "Data válida"
        data = input('Entre com uma data dd/mm/aaaa: ')
        if len(data) != 10 or data[2] != "/" or data[5] != "/":
            print('Data inválida')
            break
     
        dd = int(data[0:2])
        mm = int(data[3:5])
        aaaa = int(data[6:10])
        mensagem = ver_bissexto(aaaa)
        
        if dd < 1:
            aviso = 'Data inválida'
        elif mm < 1 or mm > 12:
            aviso = 'Data inválida'
            
        elif mm == 2 and mensagem != "bissexto" and dd > 28:
            aviso = 'Data inválida'
        
        elif mm == 2 and mensagem == "bissexto" and dd > 29:
            aviso = 'Data inválida'     
        
        elif mm % 2 == 0 and mm != 2 and dd > 30:
            aviso = 'Data inválida'
            
        elif mm % 2 != 0 and dd >31:
            aviso = 'Data inválida'
            
        print(aviso)
      
        break
               
    except ValueError:
        print('Entrada inválida!!!')
        
              
        
        
        
       
        