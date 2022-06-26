'''
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da 
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve 
ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

'''


perguntas = [ "Telefonou para a vítima? ", "Esteve no local do crime? ",
"Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]
respostas_positivas = 0

for a in range(5):
    resposta = ''
    while resposta != 'sim' and resposta != 'não':
        print(perguntas[a], end='')
        resposta = input().lower()
        if resposta == 'sim':
            respostas_positivas +=1


if respostas_positivas == 5:
    classificacao = 'Assassino'

elif respostas_positivas == 3 or respostas_positivas == 4:
    classificacao = 'Cúmplice'

elif respostas_positivas == 2:
    classificacao = 'Suspeito'

elif respostas_positivas < 2:
    classificacao = 'Inocente'

print (classificacao)
