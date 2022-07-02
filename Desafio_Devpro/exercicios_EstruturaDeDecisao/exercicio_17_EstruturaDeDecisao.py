'''
17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida
     informe se este ano é ou não bissexto.
     
     
Para ser bissexto, o ano deve ser:

    Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

    Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

    Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o
    resto igual a zero.



'''



import calendar

while True:
    try:
        ano = 0
        while ano >= 0:
            ano = int(input("Digite o ano que deseja consultar se é bissexto: "))
                

            quatro = ano % 4
            cem = ano % 100
            quatrocentos = ano % 400
            
            mensagem = calendar.isleap(ano)
            
            
            print(mensagem)
            
    except ValueError:
        print('Entrada inválida!!!')