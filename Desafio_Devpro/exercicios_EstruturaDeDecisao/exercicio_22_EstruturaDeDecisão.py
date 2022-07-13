while True:
    try:

        num = int(input('Digite o número a consultar se é par: '))

        result = num % 2

        if result == 0:
            resposta = "'Par'"
        else:
            resposta = "'Impar'"

        print(resposta)
        
    except ValueError:
        print("Entrada inválida!!!")