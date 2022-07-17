'''
19 - Altere o programa anterior
 para que ele aceite apenas 
números entre 0 e 1000. 

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

    
