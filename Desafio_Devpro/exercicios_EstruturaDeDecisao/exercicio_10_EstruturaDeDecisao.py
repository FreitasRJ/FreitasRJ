'''
10 - Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso.

'''


turno = input('Em que turno você estuda?  (M)atutino  (V)espertino (N)oturno ').lower()

if turno == 'm':
    mensagem = 'Bom Dia!'
elif turno == 'v':
    mensagem = 'Boa Tarde!'
elif turno == 'n':
    mensagem = 'Boa Noite!'
else:
    mensagem = 'Valor Inválido!'

print(mensagem)
