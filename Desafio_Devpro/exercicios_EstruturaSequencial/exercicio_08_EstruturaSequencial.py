'''
08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas
     trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
     
'''

while True:
    try:
        valor_hora = float(input('Informe o valor recebido por hora trabalhada: R$ '))
        total_hora_mes = int(input('Informe a quantidade de horas trabalhadas no mês: '))
        salario = valor_hora * total_hora_mes
        print(f'Seu salário desse mês é {salario:.2f}')
        
    except ValueError:
        print('Informe um valor válido!!!')
        break
        