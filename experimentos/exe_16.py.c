'''
16 - A série de Fibonacci é
 formada pela seqüência 
0,1,1,2,3,5,8,13,21,34,55,...
 Faça um programa que gere a 
série até que o valor seja
 maior que 500.
 



'''
primeiro = terceiro = 0
segundo = 1
conta = 0
 
try: 

    
    print('1, ', end = "")
    while terceiro < 500:
        terceiro = primeiro + segundo
        print(f'{terceiro}, ', end = "")
        primeiro , segundo = segundo , terceiro
        
    

 
       
except ValueError:
    print('Entrada inválida!!!')  