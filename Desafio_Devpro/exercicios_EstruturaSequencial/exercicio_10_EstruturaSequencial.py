'''
10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

Fórmula
    
(100 °C × 9/5) + 32 = 212 °F

'''
while True:
        try:
            cel = float(input('Informe a temperatura em Celsius a ser convertida em Fahrenheit: '))
            fahrenheit = round((cel * (9/5)) + 32)
            print(f'Essa temperatura é de {fahrenheit} Fahrenheit')
            break
        except ValueError:
            print('Valor informado ínválido!!!')
        


