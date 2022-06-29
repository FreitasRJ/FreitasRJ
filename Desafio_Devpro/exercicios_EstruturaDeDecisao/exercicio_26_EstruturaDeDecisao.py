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

peso_morango = float(input('Qual o peso dos morangos?: '))
peso_maca = float(input('Qual o peso das maças?: '))
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
    print(f'(+)  Morango  - valor:  R$  {valor_morango:.2f} - quantidade:  {peso_morango} kg - preço: R$ {preco_morango:.2f}/kg')
if peso_maca > 0:
    print(f'(+)  Maça     - valor:  R$  {valor_maca:.2f} - quantidade:  {peso_maca} kg - preço: R$ {preco_maca:.2f}/kg')


print(f'(-)  Desconto - valor:  R$  {desconto:.2f}')
print(f'          Valor Total:  R$  {preco_total:.2f}')


