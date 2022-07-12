'''
03 - Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
'''

nome =  "ff" 
idade = 155
salario = 0
sexo = 'c'
estado_civil = 'o'

while True:
    try:
        while len(nome) < 3:
            nome =  input("Entre com o nome: ")

        while idade > 150 or idade < 0:
            idade = int(input("Entre com a idade: "))

        while salario < 0:
            salario = float(input("Entre com o salario: "))
        
        while not sexo in ['f', 'm']:#sexo != 'm' and sexo != 'f':
            sexo = input('Entre com o sexo "f" ou "m": ').lower()

        while not estado_civil in ['s', 'c', 'v', 'd']:
            estado_civil = input("Entre com o estado civil: 's', 'c', 'v', 'd': ").lower()

        print('fim')
        break
    except ValueError:
        break

