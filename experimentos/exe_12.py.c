'''
12 - tabuada

'''
try:
    
    num_1 = int(input('Qual tabuada?: '))
    for tabuada in range(1,11):
        resultado = tabuada * num_1
        print(f'{num_1} X {tabuada} = {resultado}')
    
except ValueError:
    print('Entrada inválida!!!')  