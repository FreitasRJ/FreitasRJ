'''
15- A série de Fibonacci é
 formada pela seqüência
 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de 
gerar a série até o n−ésimo 
termo. 



'''
primeiro = 0
segundo = 1
conta = 0
num_termos = int(input('Fibonacci. Entre o número de temos: '))

try:
    print('1, ')
    while conta <= num_termos:
        terceiro = primeiro + segundo
        print(f'{terceiro}, ', end = "")
        primeiro = segundo
        segundo = terceiro

        
        conta += 1
    

 
       
except ValueError:
    print('Entrada inválida!!!')  