'''
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

'''
while True:
    try:
        #print('digite três números que serão apresentados em ordem decrescente.')
        n1 = float(input('Entre com o primeiro número: '))
        n2 = float(input('Entre com o segundo número: '))
        n3 = float(input('Entre com o terceiro número: '))
        
        
        # A seguir, solução que encontrei para atender ao doctest do curso
        # recebia por exemplo:
        # 10, 5.5 e 7 e pedia saida: 10, 7, 5.5
        # sem essa solução a saída seria: 10.0, 7.0, 5.0
        
                
        if round(n1) == n1:
            n1 = round(n1)
        if round(n2) ==n2:
            n2 = round(n2)
        if round(n3) == n3:
            n3 = round(n3)
            
        
              
        if n1 < n3:
            n1, n3 =  n3, n1 
        if n1 < n2:
            n1, n2 = n2, n1 
        if n2 < n3:
            n2, n3 = n3, n2
            
       
        print(f'{n1}, {n2}, {n3}')   
        break
    
    except ValueError:
        break
    
        #print('Entrada inválida!!!')        
    
    
        