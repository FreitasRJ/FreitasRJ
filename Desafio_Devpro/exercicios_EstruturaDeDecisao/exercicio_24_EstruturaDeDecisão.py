'''
24 -  Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
   operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

'''


while True:
    try:
        operacao = '?'
        num_1 = float(input('Entre com o primeiro número: '))
        
        num_2 = float(input('Entre com o segundo número: '))
        
        while not operacao in ('+', '-', '*', '/'):
            operacao = input('Entre com a operacao desejada: (+, -, / ou *): ')
         

        if operacao == '+':
            resul = num_1 + num_2
        elif operacao == '-':
            resul = num_1 - num_2
        elif operacao == '/':
            resul = num_1 / num_2
        elif operacao == '*':
            resul = num_1 * num_2

        num = round(resul)
        if resul == num:
            dec_int = 'inteiro'
        else:
            dec_int = 'decimal'

        if num < 0:
            pos_neg = 'negativo'
        if num > 0:
            pos_neg = 'positivo'            
        if num == 0:
            pos_neg = 'neutro'
            r_par_imp = 'par'
        par_imp  = resul % 2

        if par_imp == 0:
            r_par_imp = "par"       
        else:
            r_par_imp = "impar"

        if dec_int == 'decimal':
            saida = f'Número é {pos_neg} e {dec_int}'
        else:
            saida = f'Número é {r_par_imp}, {pos_neg} e {dec_int}'
        
        #-------------------------------------------------------    
        print(f'Resultado: {resul:.2f}') 
        print(saida) 
        break
    except ValueError:
        print ('Entrada inválida!!!')
