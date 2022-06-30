

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
        posicao += 1
        
    if posicao == tamanho:
        num_str += '.00'
    
    if posicao == tamanho -2:
        num_str += '0'
       
    num_espacos = num_caracteres - posicao
    num_espacos_str = '_' * num_espacos

    saida = num_espacos_str + num_str  
    return saida

valor = alinha_saida_valores_no_print(1225.1, 6)
valor2 = alinha_saida_valores_no_print(25, 6)
valor3 = alinha_saida_valores_no_print(25.3333, 6)
print(valor)
print(valor2)
print(valor3)
