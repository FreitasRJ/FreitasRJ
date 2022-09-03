import string


class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self) -> string:
        estado = 'Estou correndo...'
        return estado

    def beber(self, bebida) -> string:
        beb = bebida.capitalize()      
        if beb == 'Cerveja':
            print(self.__apresentar_documento())
            if self.idade >= 18:
                estado = (f'Estou benbendo {bebida}...')
                return estado
            else: 
                estado = (f'Não tenho idade para consumir {bebida}...')
                return estado
        estado = (f'Estou benbendo {bebida}...')
        return estado
            
    def __apresentar_documento(self):
        print(self.__cpf)

fulano = Pessoa('Fulano', 17, '098098jfdf')
print(fulano.correr())
print(fulano.beber('cerveja'))
print(fulano.beber('água'))


