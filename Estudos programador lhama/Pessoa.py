'''
Programação Orientada a Objetos:
        Pilares:

        * Encapsulamento

        * Polimorfismo

        * Herança

        * Abstração (???)
                        **************************
Objeto                  *       Classe           *
Fora do contexto -->    * [Dentro do Contexto]   *
                        **************************

---------------------------------
|            Pessoa              |
--------------------------------- 
| + nome: string                 |
| + idade: number                | Diagrama UML
| - cpf: string                  | obs.: + publico - elemento privado (Acesso somente na classe.)
---------------------------------
| + Correr(): Nome               |   
| + beber(bebida:string)         |
| - apresentar_documento(): None |
|--------------------------------|

'''

class Pessoa:
    def __init__(self, nome, idade,cpf) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf # self.__cpf declara cpf como privado

    #def print_cpf(self):
     #   print(self.__cpf)

    def correr(self):
        print('Correndo...')

    def beber(self, bebida):
        if bebida == "cerveja":
           self.__apresentar_documento()
        print(f'Bebendo...{bebida}')


    def __apresentar_documento(self):
        print(self.__cpf)

  
ronaldo = Pessoa('Ronaldo', 32, '1234567891-0')
ronaldo.correr()
#ronaldo.print_cpf()
ronaldo.beber('cerveja')
ronaldo.beber('água')



    

