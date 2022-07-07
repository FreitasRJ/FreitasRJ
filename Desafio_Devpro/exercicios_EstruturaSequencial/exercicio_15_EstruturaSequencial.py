'''
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido. 
'''

while True:
    try:
        valor_hora = float(input('Informe o valor recebido por hora trabalhada: R$ '))
        total_hora_mes = int(input('Informe a quantidade de horas trabalhadas no mês: '))
        salario = valor_hora * total_hora_mes
        print(f'Salário do mês é: {salario}')
        
        imposto_renda = salario * .11
        inss = salario * .08
        sindicato = salario *.05
        salario_liquido = salario - imposto_renda - inss - sindicato

        print(f'+ Salário Bruto :   R$ {salario}')
        print(f'- IR (11%) :        R$ {imposto_renda}')
        print(f'- INSS (8%) :       R$ {inss}')
        print(f'- Sindicato ( 5%) : R$ {sindicato}')
        print(f'= Salário Liquido : R$ {salario_liquido}')

    except ValueError:
        print('Informe um valor válido!!!')
        break