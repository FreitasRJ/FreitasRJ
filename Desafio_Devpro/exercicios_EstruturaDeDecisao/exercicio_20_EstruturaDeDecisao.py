'''
20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média
    alcançada por aluno e presentar:

    a - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    b - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    c - A mensagem "Aprovado com Distinção", se a média for igual a 10.
    
'''

while True:
    try:
        nota_1 = float(input("Informe a primeira nota: "))
        nota_2 = float(input("Informe a segunda nota: "))
        nota_3 = float(input("Informe a terceira nota: "))
        
        media = (nota_1 + nota_2 + nota_3)/3
        
        if media == 10:
            situacao = 'Aprovado com Distinção'
        elif media >= 7:
            situacao = 'Aprovado'
        elif media < 7:
            situacao = 'Reprovado'
        
        #retirado para atender o doctest do curso.
        #print(f'{situacao} com média alcançada {media:.2f}.')
        print(situacao)
        break       
    except ValueError:
        print('Entrada inválida!!!')