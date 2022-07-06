"""
2 -  Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
while True:
    nome = senha = "nome"
    while nome == senha:
        nome = input("Entre com o nome de usuário: ")
        senha = input("Entre com a senha: ")
        if nome == senha:
            print("Erro! Nome e senha devem ser diferente.")
    break
