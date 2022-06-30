

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
        if num_str[posicao] != '.':
            #inteiro += num_str[posicao]
            posicao += 1
        else:
            # resolver quando entrada = nn.n ou nn
            
            pass    
    num_espacos = num_caracteres - posicao
    num_espacos_str = '_' * num_espacos

    saida = num_espacos_str + num_str  
    return saida

valor = alinha_saida_valores_no_print(1225.14, 6)
valor2 = alinha_saida_valores_no_print(25.12, 6)
print(valor)
print(valor2)

