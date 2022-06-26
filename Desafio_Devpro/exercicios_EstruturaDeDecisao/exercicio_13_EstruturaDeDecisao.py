"""
Exercício 13 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

    
"""

while True:
    try:
        # dia = 0
        dia = int(input('Digite um número entre 1 e 7: '))
      
      
        if  dia < 1 or dia >7:
            print('Dia Inválido')

        elif dia == 1:
            print('Domingo')
        elif dia == 2:
            print('Segunda')
        elif dia == 3:
            print('Terça')
        elif dia == 4:
            print('Quarta')
        elif dia == 5:
            print('Quinta')
        elif dia == 6:
            print('Sexta')
        elif dia == 7:
            print('Sábado')
        
    except ValueError:
        print('Dia Inválido')
        