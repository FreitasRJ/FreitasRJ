'''    
    Exercício 27 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
    ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade 
(em Kg) de maças
adquiridas e escreva o
valor a ser pago pelo cliente.
Mostre o restultado com duas casas decimais
'''


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

def alinha_a_direita(dado: str, num_caracteres: int):
    ''' Alinha dados a direita em uma coluna formada por num_caracteres.
           ex.: "100", 3 --> 100
                 "10", 3 -->  10
                  "1", 3 -->   1
    '''
    
    tamanho = len(dado)
    inteiro = ''

    num_espacos = num_caracteres - tamanho
    num_espacos_str = ' ' * num_espacos
    alinhado = num_espacos_str + dado  
    return alinhado



peso_morango = int(input('Qual o peso dos morangos?: '))
peso_maca = int(input('Qual o peso das maças?: '))
desconto = 0

preco_morango = 2.5
preco_maca = 1.80

if peso_morango > 5:
    preco_morango = 2.2
if peso_maca > 5:
    preco_maca = 1.5

valor_maca = preco_maca * peso_maca
valor_morango = preco_morango * peso_morango

peso_total = peso_maca + peso_morango
preco_total = valor_maca + valor_morango

if preco_total > 25 or peso_total > 8:
    desconto = (preco_total * .1)
    preco_total -= desconto



if peso_morango > 0:
    valor_morango_str = alinha_saida_valores_no_print(valor_morango, 2)
    preco_morango_str = alinha_saida_valores_no_print(preco_morango, 2)
    peso_morango_str = alinha_a_direita (str(peso_morango), 3)
    print(f'(+)  Morango  - valor:  R$  {valor_morango_str} - quantidade:  {peso_morango_str} kg - preço: R${preco_morango_str}/kg')

if peso_maca > 0:
    valor_maca_str = alinha_saida_valores_no_print(valor_maca, 2)
    preco_maca_str = alinha_saida_valores_no_print(preco_maca, 2)
    peso_maca_str = alinha_a_direita (str(peso_maca), 3)
    print(f'(+)  Maça     - valor:  R$  {valor_maca_str} - quantidade:  {peso_maca_str} kg - preço: R${preco_maca_str}/kg')

desconto_str = alinha_saida_valores_no_print(desconto, 2)
preco_total_str = alinha_saida_valores_no_print(preco_total, 2)

print(f'(-)  Desconto - valor:  R$  {desconto_str}')
print(f'          Valor Total:  R$  {preco_total_str}')


