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
        while not operacao in ('+', '-', '*', '/'):
            operacao = input('Entre com a operacao desejada: (+, -, / ou *): ')
        
        num_2 = float(input('Entre com o segundo número: '))
   

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

        if resul < 0:
            pos_neg = 'negativo'
        else:
            pos_neg = 'positivo'

        par_imp  = resul % 2

        if par_imp == 0:
            r_par_imp = "par"       
        else:
            r_par_imp = "impar"
        # para atender ao doctest do curso, apesar de zero ser par, 
        # declaro como neutro:
        # -1, 0, 1 --> número par fica entre impares. 
        if resul == 0:
            r_par_imp = 'neutro'
        #-------------------------------------------------------    
        print(f'Resultado: {resul:.2f}') 
        print(f'Número é {r_par_imp}, {pos_neg} e {dec_int}') 
        break
    except ValueError:
        print ('Entrada inválida!!!')
