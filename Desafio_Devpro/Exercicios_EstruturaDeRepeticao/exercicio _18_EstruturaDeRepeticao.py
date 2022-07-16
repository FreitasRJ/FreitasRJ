'''
18 - Faça um programa que, 
dado um conjunto de N números,
 determine o menor valor, o 
maior valor e a soma dos
 valores. 

'''
def sort(fila):
    tam = len(fila)
    soma= fila[0]
    maior = menor = fila[0]
    
    
    for index in range(1, tam):
        soma += fila[index]
        if fila[index] > maior:
            maior = fila[index]
            
        if fila[index] < menor:
            menor =  fila[index]
        
        if  maior < menor:
            maior, menor = menor, maior 
    
    print(fila)
    print(maior, menor)
    print(f'Soma: {soma}')
    
    
conjunto = [9,8,7,6,5,4,3,2,10, -2]
print (sort(conjunto))

    
