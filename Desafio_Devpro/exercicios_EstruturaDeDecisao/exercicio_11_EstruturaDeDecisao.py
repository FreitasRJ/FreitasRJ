'''
11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
no salário atual:

  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5%
  
  Após o aumento ser realizado, informe na tela:
  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.

Mostrar valores monetários com duas casas decimais.

'''
while True:
    try:
        
        salario = float(input('Digite o salário atual do colaborador ou 0 para terminar: R$ '))
        #if salario == 0:
         #   break
        
    except ValueError:
        break
        #Print('Entrada inválida!!!')

    novo_salario = 0
    ajuste = 0

    if salario <= 280:
        ajuste = 20
        valor_aumento = salario * (ajuste/100)
        novo_salario = salario + valor_aumento
        
    elif 280 < salario <= 700:
        ajuste = 15
        valor_aumento = salario * (ajuste/100)
        novo_salario = salario + valor_aumento

    elif 700 < salario <= 1500:
        ajuste = 10
        valor_aumento = salario * (ajuste/100)
        novo_salario = salario + valor_aumento

    elif  salario > 1500:
        ajuste = 5
        valor_aumento = salario * (ajuste/100)
        novo_salario = salario + valor_aumento
        
       
    print(f'Salário atual: R$ {salario:.2f}')
    print(f'Aumento porcentual: {ajuste}%')
    print(f'Valor do aumento: R$ {valor_aumento:.2f}')
    print(f'Novo salário: R$ {novo_salario:.2f}')
    
    break
