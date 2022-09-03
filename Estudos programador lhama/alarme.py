# Aula vídeo 04 - Orientação a Objetos em Python - Getters / Setters e Estados
# conceito de estado.
class Alarm:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado
    
    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> bool:
        if isinstance(valor, bool):
            self.__estado = valor

clock = Alarm(True)
# armado = clock.__estado Não funciona devido ao estado estar privado.
armado = clock.get_estado()
print(armado)

# alterando o estado.
clock.set_estado(False)
armado = clock.get_estado()
print(armado)

# não altera, pois não foi fornecido um booleano.
clock.set_estado('não boleano')
armado = clock.get_estado()
print(armado)