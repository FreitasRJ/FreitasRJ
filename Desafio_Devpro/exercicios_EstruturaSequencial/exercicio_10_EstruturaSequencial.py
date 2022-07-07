'''
10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Fórmula
    
(100 °C × 9/5) + 32 = 212 °F

'''
while True:
        try:
            cel = float(input('Informe a temperatura em Celsius a ser convertida em Fahrenheit: '))
            # print(f'O equivalente a {cel} Fahrenheit em Fahrenheit é { (cel * (9/5)) + 32}')
            print(f'Essa temperatura é de {(cel * (9/5)) + 32} Fahrenheit')
        except ValueError:
            print('Valor informado ínválido!!!')
        


