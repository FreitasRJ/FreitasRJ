'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''


vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']

while True:

    letra = input("Digite uma letra: ").lower()    

    if letra in vogais:
    
        #print(f'A letra {letra} é uma vogal')
        print('vogal')
        
    elif letra in consoantes:
        
         #print(f'A letra {letra} é uma consoante')
        print('consoante')
    #else:
    
       #break
    
   
    
