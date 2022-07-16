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
    
conjunto = []   
conjunto_original = [4,1,6,1001,11,55,-2,1000]
for novo in range(0,len(conjunto_original)):
    novo = conjunto_original[novo]
    if novo >= 0 and novo <= 1000:
        conjunto.append(novo)
    print(conjunto)

print (sort(conjunto))

    
