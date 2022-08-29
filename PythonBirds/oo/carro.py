'''
    Você deve criar uma classe carro  que vai possuir dois atributos
compostos por outras duas classes:

1 -  Motor  
2 -  Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1 - Atributo de dado velocidade
2 - Método acelerar,. que deverá incrementar a velocidade de uma unidade
3 - Método frear que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de contraolar a direção. Ela oferece os 
seguintes atributos:

1 - Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2 - Método girar a direita,
3 - Método girar a esquerda.

  N
O   L
  S

    Exemplo:
    # testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'

    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcula_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcula_direcao()
    >>> 'Norte'
    >>> carro.gira_a_direita()
    >>> carro.calcula_direcao()
    >>> 'Leste'
    >>> carro.gira_a_esquerda()
    >>> carro.calcula_direcao()
    >>> 'Norte'
    >>> carro.gira_a_esquerda()
    >>> carro.calcula_direcao()
    >>> 'Oeste'

'''

chave = 0

class Motor:
    def __init__(self):
        self.velocidade = 0
        

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0
    
class Direcao:
   
    def __init__(self):
        rumo = {1:'Norte', 2:'Leste', 3:'Sul', 4:'Oeste'}
        self.valor = rumo[1]
        
    def girar_a_direita(self):
        chave +=1
        if chave > 4:
            chave = 1
        self.valor = rumo[chave]

print(chave)
a = Direcao()
a.girar_a_direita()

