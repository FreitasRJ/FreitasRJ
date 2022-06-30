def alinha_a_direita(dado: str, num_caracteres: int):
    ''' Resulta em alinhamento das colunas de impressão de valores com número
        de caracteres diferente. Retornando uma string do tamanho indicado em
        num_caracters.
    '''
    
    tamanho = len(dado)
    inteiro = ''

    num_espacos = num_caracteres - tamanho
    num_espacos_str = ' ' * num_espacos
    alinhado = num_espacos_str + dado  
    return alinhado


valor = alinha_a_direita("100", 3)
valor2 = alinha_a_direita("10", 3)
valor3 = alinha_a_direita("1", 3)
print(valor)
print(valor2)
print(valor3)