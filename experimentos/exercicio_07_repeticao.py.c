'''
07 repetição Faça um programa 
que leia 5 números e informe
 o maior número.
'''
lista = []
for a in range(1,6):
    numero = input(f'Informe o número {a}:  ')
    lista.append(numero)
   
a, b, c, d, e = int(lista[0]), int(lista[1]), int(lista[2]), int(lista[3]), int(lista[4])

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if d > e:
    d, e = e, d
print(f'O maior número da lista é: {e}')

    