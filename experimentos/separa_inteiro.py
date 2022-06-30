

def alinha_saida_valores_no_print(numero: float, num_caracteres: int):
    ''' Resulta em alinhamento das colunas de impressão de valores com número
        de caracteres diferente. Retornando uma string do tamanho indicado em
        num_caracters.
    '''
    
    num_str = str(numero)
    tamanho = len(num_str)
    posicao = 0
    inteiro = ''

    while posicao < tamanho and num_str[posicao] != '.':
        inteiro += num_str[posicao]
        posicao += 1      
        
    if posicao == tamanho:
        num_str += '.00'
    
    elif posicao == tamanho - 2:
        num_str += '0'
    
    elif num_str[posicao] == '.' and tamanho - posicao - 1 >= 2:
        num_str = inteiro + num_str[posicao] + num_str[posicao + 1] + num_str[posicao + 2]       
       
 
    num_espacos = num_caracteres - posicao
    num_espacos_str = ' ' * num_espacos

    saida = num_espacos_str + num_str  
    return saida


valor = alinha_saida_valores_no_print(5.1, 6)
valor2 = alinha_saida_valores_no_print(25, 6)
valor3 = alinha_saida_valores_no_print(25.333, 6)
print(valor)
print(valor2)
print(valor3)
