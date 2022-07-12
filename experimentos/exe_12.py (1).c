'''
12 - tabuada

'''
try:
    num_1 = 0
    while num_1 < 1 or num_1 > 10:
        num_1 = int(input('Qual tabuada? Entre 1 e 10: '))
    for tabuada in range(1,11):
        resultado = tabuada * num_1
        print(f'{num_1} X {tabuada} = {resultado}')
    
except ValueError:
    print('Entrada inválida!!!')  