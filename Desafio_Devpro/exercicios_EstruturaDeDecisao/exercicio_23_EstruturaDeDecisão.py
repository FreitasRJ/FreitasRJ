while True:
    try:

        numero = float(input('digite um número: '))
        num = round(numero)
        if numero == num:
            print('Inteiro')
        else:
            print('Decimal') 
    except ValueError:
        print('Entrada inválida')
        