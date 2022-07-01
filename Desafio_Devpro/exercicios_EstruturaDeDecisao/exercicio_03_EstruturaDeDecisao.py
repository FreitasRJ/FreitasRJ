"""
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

"""

while True:

    sexo = input('Digite: (F) - Feminino ou  (M) - Masculino:  ').lower()

    if sexo == 'f':
        print('F - Feminino')
    
    elif sexo == 'm':
        print('M - Masculino')
    
    elif 'f' != sexo != 'm':

        print('Sexo Inválido')
        
