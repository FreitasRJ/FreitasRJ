'''
SOLID is an acronym that stands for the following:

    * Single responsibility principle (Princípio da resposabilidade única.)
    * Open/closed principle
    * Liskov substitution principle
    * Interface segregation principle
    * Dependency inversion principle

 


# SRP
# Exemplo de código que não atende.

class SistemaCadastral:

    def cadastrar(nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('Acessando o banco de dados...')
            print(f'Cadastrando usuário {nome} idade {idade}')
        else:
            print('Dados inválidos!')

registro = SistemaCadastral
registro.cadastrar("Fábio",51)

'''

# Forma de acordo com o SRP

class SistemaCadastral:

    def cadastrar(self, nome: str,idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_dados(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome:str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_dados(self,nome: str, idade: int) -> None:
        print('Acessando o banco de dados...')
        print(f'Cadastrando usuário {nome} idade {idade}')        
    
    def __indicar_erro(self) -> None:
        print('Dados inválidos!')


sis = SistemaCadastral()
sis.cadastrar("Fábio", 51)
sis.cadastrar(22,22)


        
        